from PIL import Image
from pathlib import Path
import matplotlib.pyplot as plt


def compress_image(input_path: Path):
    img = Image.open(input_path)

    compression_ratios = list(range(10, 101, 10))
    base_dir = input_path.parent
    file_sizes = {}

    for cr in compression_ratios:
        quality = max(1, 100 - cr)
        output_path = base_dir / f"comp-{cr}.jpg"
        img.save(output_path, "JPEG", quality=quality)
        size = output_path.stat().st_size
        file_sizes[cr] = size
        print(
            f"Saved {output_path} (compression ratio={cr}%, quality={quality}, size={size} bytes)"
        )

    compression_sorted = sorted(file_sizes.keys())
    sizes = [file_sizes[cr] for cr in compression_sorted]

    plt.figure(figsize=(8, 6))
    plt.plot(compression_sorted, sizes, marker="o")
    plt.xlabel("Compression Ratio (%)")
    plt.ylabel("File Size (bytes)")
    plt.grid(True)

    # グラフ画像として保存
    graph_path = base_dir / "compression_graph.svg"
    plt.savefig(graph_path)
    print(f"Graph saved at {graph_path}")

    plt.show()


def main():
    input_path = Path.cwd() / "img" / "original.jpg"
    compress_image(input_path)


if __name__ == "__main__":
    main()
