import os

# 定义层级结构
base_folders = ['screenshots', 'recordings']
sub_folders = ['P0', 'P1', 'P2']

def create_folders():
    for base in base_folders:
        for sub in sub_folders:
            # 组合路径，例如：screenshots/P0
            path = os.path.join(base, sub)
            
            # 创建文件夹
            os.makedirs(path, exist_ok=True)
            
            # 创建 .gitkeep 文件（Git 不追踪空文件夹，所以必须有个文件占位）
            keep_file = os.path.join(path, '.gitkeep')
            with open(keep_file, 'w') as f:
                pass
            
    print("✅ 文件夹结构创建成功！")
    print("已生成：")
    for base in base_folders:
        print(f"  - {base}/ [P0, P1, P2]")

if __name__ == "__main__":
    create_folders()
