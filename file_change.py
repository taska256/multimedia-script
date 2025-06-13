from PIL import Image
from pathlib import Path
import matplotlib.pyplot as plt


def convert_and_compare(input_path: Path):
    img = Image.open(input_path)
    base_dir = input_path.parent
    file_sizes = {}

    # オリジナルJPEGのファイルサイズを取得して比較に含める
    original_size = input_path.stat().st_size
    file_sizes["JPEG"] = original_size
    print(f"Original JPEG: {input_path} (size: {original_size} bytes)")

    # 変換先のフォーマット一覧
    formats = ["GIF", "PNG", "BMP", "WEBP"]
    for fmt in formats:
        extension = fmt.lower()
        output_path = base_dir / f"original_converted.{extension}"
        # 必要に応じて img.convert("RGB") を追加
        img.save(output_path, fmt)
        size = output_path.stat().st_size
        file_sizes[fmt] = size
        print(f"Converted to {fmt}: {output_path} (size: {size} bytes)")

    return file_sizes


def plot_file_sizes(file_sizes: dict):
    formats = list(file_sizes.keys())
    sizes = [file_sizes[fmt] for fmt in formats]

    plt.figure(figsize=(8, 6))
    plt.bar(formats, sizes, color="skyblue")
    plt.xlabel("File Format")
    plt.ylabel("File Size (bytes)")
    plt.grid(True, axis="y", linestyle="--", alpha=0.7)

    # グラフ画像として保存
    base_dir = Path.cwd() / "img"
    graph_path = base_dir / "formats_comparison.svg"
    plt.savefig(graph_path)
    print(f"Graph saved at {graph_path}")

    plt.show()


def main():
    input_path = Path.cwd() / "img" / "original.jpg"
    file_sizes = convert_and_compare(input_path)
    plot_file_sizes(file_sizes)


if __name__ == "__main__":
    main()
