import os
import random
from PIL import Image

def rotate_image(image_path, angle=90):
    """Xoay ảnh theo góc cho trước.

    Args:
        image_path: Đường dẫn đến ảnh.
        angle: Góc xoay (mặc định là 90 độ).
    """
    image = Image.open(image_path)
    rotated_image = image.rotate(angle)
    return rotated_image

def combine_images(image1_path, image2_path, output_path, target_size=(19630, 15529), dpi=300):
    """Ghép hai ảnh đã xoay thành một, với kích thước và độ phân giải tùy chỉnh.

    Args:
        image1_path: Đường dẫn đến ảnh thứ nhất.
        image2_path: Đường dẫn đến ảnh thứ hai.
        output_path: Đường dẫn để lưu ảnh kết quả.
        target_size: Kích thước mong muốn của ảnh kết quả (width, height).
        dpi: Độ phân giải của ảnh kết quả.
    """
    image1 = rotate_image(image1_path)
    image2 = rotate_image(image2_path)

    # Tạo ảnh mới với kích thước và độ phân giải mong muốn
    new_image = Image.new('RGB', target_size)

    # Tính toán vị trí đặt ảnh vào ảnh mới (giả sử đặt hai ảnh cạnh nhau)
    x1, y1 = 276, 1060
    x2, y2 = 9928, 1060

    # Ghép ảnh vào ảnh mới
    new_image.paste(image1, (x1, y1))
    new_image.paste(image2, (x2, y2))

    # Lưu ảnh kết quả với độ phân giải đã cho
    new_image.save(output_path, dpi=dpi)

if __name__ == "__main__":
    folder_path = input("Nhập đường dẫn đến folder chứa ảnh: ")
