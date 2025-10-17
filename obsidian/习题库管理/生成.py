# generate_problems.py
import os
from config import subjects

# 创建题目列表文件夹
OUTPUT_DIR = "题目列表"
os.makedirs(OUTPUT_DIR, exist_ok=True)  # 如果文件夹不存在则创建


def file_exists_and_has_content(filename):
	"""检查文件是否存在且包含完成标记"""
	if not os.path.exists(filename):
		return False
	try:
		with open(filename, 'r', encoding='utf-8') as f:
			content = f.read()
			return '[x]' in content  # 如果文件中有完成的题目，就不覆盖
	except:
		return False


def generate_simple_subject(subject_name, data,
                            chapter_names):
	"""生成简单结构的题目列表（不覆盖已有进度）"""
	filename = os.path.join(OUTPUT_DIR,
	                        f"{subject_name}题目列表.md")  # 修改这里

	# 如果文件已存在且有完成进度，就不重新生成
	if file_exists_and_has_content(filename):
		print(
			f"⚠️  {subject_name}: {filename} 已存在且有完成进度，跳过生成")
		return filename

	content = f"# {subject_name}题目列表\n\n"

	for i, (total_problems, chapter_name) in enumerate(
			zip(data, chapter_names), 1):
		content += f"## 第{i}章 {chapter_name}\n\n"
		for j in range(1, total_problems + 1):
			content += f"- [ ] {i}.{j}\n"
		content += "\n"

	with open(filename, "w", encoding="utf-8") as f:
		f.write(content)

	print(f"✅ {subject_name}: 已生成 {filename}")
	return filename


def generate_detailed_subject(subject_name, data):
	"""生成详细结构的题目列表（不覆盖已有进度）"""
	filename = os.path.join(OUTPUT_DIR,
	                        f"{subject_name}题目列表.md")  # 修改这里

	# 如果文件已存在且有完成进度，就不重新生成
	if file_exists_and_has_content(filename):
		print(
			f"⚠️  {subject_name}: {filename} 已存在且有完成进度，跳过生成")
		return filename

	content = f"# {subject_name}题目列表\n\n"

	for i, (chapter_name, sections) in enumerate(data, 1):
		content += f"## 第{i}章 {chapter_name}\n\n"

		for sec_idx, sec_problems in enumerate(sections, 1):
			content += f"### {i}.{sec_idx}\n"
			for prob_idx in range(1, sec_problems + 1):
				content += f"- [ ] {i}.{sec_idx}.{prob_idx}\n"
			content += "\n"

	with open(filename, "w", encoding="utf-8") as f:
		f.write(content)

	print(f"✅ {subject_name}: 已生成 {filename}")
	return filename


def generate_missing_only():
	"""只生成缺失的文件，不覆盖已有文件"""
	for subject_name, subject_info in subjects.items():
		filename = os.path.join(OUTPUT_DIR,
		                        f"{subject_name}题目列表.md")  # 修改这里

		if not os.path.exists(filename):
			# 文件不存在，生成新文件
			if subject_info["type"] == "simple":
				generate_simple_subject(
					subject_name,
					subject_info["data"],
					subject_info["chapter_names"]
				)
			else:
				generate_detailed_subject(
					subject_name,
					subject_info["data"]
				)
		else:
			# 文件存在，检查是否有完成进度
			if file_exists_and_has_content(filename):
				print(
					f"⚠️  {subject_name}: {filename} 已存在且有完成进度，跳过生成")
			else:
				print(
					f"📄 {subject_name}: {filename} 已存在但无完成进度，跳过生成")


def main():
	"""主函数"""
	print("=== 题目列表生成器 ===\n")

	# 只生成缺失的文件
	generate_missing_only()

	# 统计信息
	print("\n=== 统计信息 ===")
	for subject_name, subject_info in subjects.items():
		filename = os.path.join(OUTPUT_DIR,
		                        f"{subject_name}题目列表.md")  # 修改这里
		exists = os.path.exists(filename)

		if subject_info["type"] == "simple":
			total = sum(subject_info["data"])
		else:
			total = sum(sum(sections) for _, sections in
			            subject_info["data"])

		status = "✅ 已存在" if exists else "❌ 缺失"
		print(f"{subject_name}: {status} (共{total}题)")

	print(f"\n文件保存在: {os.path.abspath(OUTPUT_DIR)}")


if __name__ == "__main__":
	main()