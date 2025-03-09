def change_csv_delimiter(input_file, output_file, old_delim=',', new_delim=';'):
    """
    不使用 csv 库，手动修改 CSV 文件的分隔符
    :param input_file: 原始 CSV 文件路径
    :param output_file: 修改后 CSV 文件路径
    :param old_delim: 旧的分隔符（默认 `,`）
    :param new_delim: 新的分隔符（默认 `;`）
    """
    with open(input_file, 'r', encoding='utf-8-sig') as infile, \
         open(output_file, 'w', encoding='utf-8-sig') as outfile:
        
        for line in infile:
            new_line = line.strip().replace(old_delim, new_delim)  # 替换分隔符
            outfile.write(new_line + new_delim + '\n')  # 写入新文件

    print(f"✅ CSV 文件已转换：{input_file} → {output_file}（{old_delim} → {new_delim}）")

# 示例用法
input_csv = "data_raw.txt"   # 输入文件
output_csv = "data.txt"  # 输出文件
change_csv_delimiter(input_csv, output_csv, old_delim=' ', new_delim=',')
