# check_progress.py
import os
import re
import matplotlib.pyplot as plt
import matplotlib as mpl
import sys
from config import subjects

# 设置中文字体
mpl.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
mpl.rcParams['axes.unicode_minus'] = False

# 题目列表文件夹路径
OUTPUT_DIR = "题目列表"

def analyze_simple_progress(filename, data, chapter_names):
    """分析简单结构的进度"""
    if not os.path.exists(filename):
        return None, None

    completed = [0] * len(data)

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'- \[x\] (\d+)\.\d+'
    matches = re.findall(pattern, content)

    for chap_str in matches:
        chap = int(chap_str) - 1
        if 0 <= chap < len(data):
            completed[chap] += 1

    rates = [c / t if t > 0 else 0 for c, t in zip(completed, data)]
    return completed, rates

def analyze_detailed_progress(filename, data):
    """分析详细结构的进度"""
    if not os.path.exists(filename):
        return None, None, None

    completed = [[0] * len(sections) for _, sections in data]

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'- \[x\] (\d+)\.(\d+)\.\d+'
    matches = re.findall(pattern, content)

    for chap_str, sec_str in matches:
        chap = int(chap_str) - 1
        sec = int(sec_str) - 1
        if 0 <= chap < len(data) and 0 <= sec < len(data[chap][1]):
            completed[chap][sec] += 1

    # 计算每个小节的完成率
    section_rates = []
    for chap_idx, (sections_completed, (_, sections_data)) in enumerate(zip(completed, data)):
        chap_rates = [c / t if t > 0 else 0 for c, t in zip(sections_completed, sections_data)]
        section_rates.append(chap_rates)

    # 计算每个章节的总完成率
    chapter_rates = []
    for chap_idx, (sections_completed, (_, sections_data)) in enumerate(zip(completed, data)):
        total_completed = sum(sections_completed)
        total_problems = sum(sections_data)
        chapter_rates.append(total_completed / total_problems if total_problems > 0 else 0)

    return completed, section_rates, chapter_rates

def print_simple_statistics(subject_name, data, chapter_names, completed, rates):
    """打印简单结构的统计信息"""
    total_problems = sum(data)
    total_completed = sum(completed)
    overall_rate = total_completed / total_problems if total_problems > 0 else 0

    print(f"\n📊 {subject_name} 进度统计:")
    print(f"   总题目: {total_problems}")
    print(f"   已完成: {total_completed}")
    print(f"   完成率: {overall_rate:.1%}")

    print("\n   按章节统计:")
    for i, (chap_completed, chap_total, rate) in enumerate(zip(completed, data, rates)):
        chap_name = chapter_names[i]
        print(f"     {i + 1}. {chap_name}: {chap_completed}/{chap_total} ({rate:.1%})")

def print_detailed_statistics(subject_name, data, completed, chapter_rates):
    """打印详细结构的统计信息"""
    total_problems = sum(sum(sections) for _, sections in data)
    total_completed = sum(sum(chap) for chap in completed)
    overall_rate = total_completed / total_problems if total_problems > 0 else 0

    print(f"\n📊 {subject_name} 进度统计:")
    print(f"   总题目: {total_problems}")
    print(f"   已完成: {total_completed}")
    print(f"   完成率: {overall_rate:.1%}")

    print("\n   按章节统计:")
    for i, (chap_completed, (chap_name, sections_data), rate) in enumerate(zip(completed, data, chapter_rates)):
        chap_total = sum(sections_data)
        chap_done = sum(chap_completed)
        print(f"     {i + 1}. {chap_name}: {chap_done}/{chap_total} ({rate:.1%})")

def plot_subject_progress(subject_name, subject_info, completed_data):
    """绘制单个科目的进度图"""
    if completed_data[0] is None:
        print(f"❌ {subject_name}: 无法分析进度，文件可能不存在")
        return

    plt.figure(figsize=(10, 6))

    if subject_info["type"] == "simple":
        completed, rates = completed_data
        data = subject_info["data"]
        chapter_names = [f'{i + 1}.{name}' for i, name in enumerate(subject_info["chapter_names"])]

        bars = plt.bar(chapter_names, rates, color=plt.cm.RdYlGn(rates), alpha=0.7, edgecolor='black')
        plt.title(f'{subject_name} - 章节完成率')
        plt.ylim(0, 1.1)
        plt.xticks(rotation=45)

        for bar, rate, c, t in zip(bars, rates, completed, data):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02,
                    f'{c}/{t}', ha='center', va='bottom', fontsize=9)

    else:
        completed, section_rates, chapter_rates = completed_data
        data = subject_info["data"]
        chapter_names = [f'{i + 1}.{name}' for i, (name, _) in enumerate(data)]

        bars = plt.bar(chapter_names, chapter_rates, color=plt.cm.RdYlGn(chapter_rates), alpha=0.7, edgecolor='black')
        plt.title(f'{subject_name} - 章节完成率')
        plt.ylim(0, 1.1)
        plt.xticks(rotation=45)

        for i, (bar, rate) in enumerate(zip(bars, chapter_rates)):
            chap_completed = sum(completed[i])
            chap_total = sum(data[i][1])
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02,
                    f'{chap_completed}/{chap_total}', ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.show()

def analyze_single_subject(subject_name):
    """分析单个科目的进度"""
    if subject_name not in subjects:
        print(f"❌ 科目 '{subject_name}' 不存在")
        print("可用科目:", ", ".join(subjects.keys()))
        return

    subject_info = subjects[subject_name]
    filename = os.path.join(OUTPUT_DIR, f"{subject_name}题目列表.md")  # 修改这里

    if not os.path.exists(filename):
        print(f"❌ {subject_name}: 文件不存在")
        print(f"   预期路径: {os.path.abspath(filename)}")
        return

    print(f"🔍 检查 {subject_name}...")

    if subject_info["type"] == "simple":
        completed_data = analyze_simple_progress(filename, subject_info["data"], subject_info["chapter_names"])
        if completed_data[0] is not None:
            print_simple_statistics(subject_name, subject_info["data"], subject_info["chapter_names"], *completed_data)
            plot_subject_progress(subject_name, subject_info, completed_data)
    else:
        completed_data = analyze_detailed_progress(filename, subject_info["data"])
        if completed_data[0] is not None:
            completed, section_rates, chapter_rates = completed_data
            print_detailed_statistics(subject_name, subject_info["data"], completed, chapter_rates)
            plot_subject_progress(subject_name, subject_info, completed_data)

def analyze_all_subjects():
    """分析所有科目的进度"""
    print("=== 所有科目进度检查 ===")
    for subject_name in subjects.keys():
        analyze_single_subject(subject_name)

def main():
    """主函数"""
    # 检查命令行参数
    if len(sys.argv) > 1:
        # 有参数：分析指定科目
        subject_name = sys.argv[1]
        analyze_single_subject(subject_name)
    else:
        # 无参数：显示选择菜单
        print("=== 刷题进度检查 ===")
        print("请选择要分析的科目:")
        subject_list = list(subjects.keys())
        for i, subject in enumerate(subject_list, 1):
            print(f"  {i}. {subject}")
        print(f"  {len(subject_list) + 1}. 所有科目")

        try:
            choice = input("\n请输入选择编号: ").strip()
            if choice.isdigit():
                choice_num = int(choice)
                if 1 <= choice_num <= len(subject_list):
                    analyze_single_subject(subject_list[choice_num - 1])
                elif choice_num == len(subject_list) + 1:
                    analyze_all_subjects()
                else:
                    print("❌ 无效的选择")
            else:
                print("❌ 请输入数字")
        except KeyboardInterrupt:
            print("\n👋 已退出")

if __name__ == "__main__":
    main()