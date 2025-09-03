

from PIL import Image

# ASCII characters used to build the output text
ASCII_CHARS = ["Ñ", "@", "#", "W", "$", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0", "?", "a", "b", "c", ";", ":", "+", "=", "-", ",", ".", "_"]

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(ratio * new_width)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Convert each pixel to grayscale
def grayify(image):

    return image.convert("L")


# Convert pixels to a string of ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    # Map pixel value (0-255) to ASCII_CHARS index (0 to len(ASCII_CHARS)-1)
    characters = "".join([ASCII_CHARS[pixel * (len(ASCII_CHARS) - 1) // 255] for pixel in pixels])
    return characters


# Main function to handle the process
def main():
    path = input("Enter a valid path to an image (e.g., img/images.jpeg):\n")
    try:
        image = Image.open(path)
    except Exception as e:
        print(path, "is not a valid pathname to an image.")
        return

    new_width = 100
    try:
        new_width = int(input("Enter desired ASCII art width (default 100): ") or "100")
    except ValueError:
        print("Invalid width, using default 100.")

    image = resize_image(image, new_width)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    pixel_count = len(ascii_str)
    ascii_image = "\n".join(ascii_str[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    print(ascii_image)
    with open("ascii_image.txt", "w", encoding="utf-8") as f:
        f.write(ascii_image)
    print("ASCII art written to ascii_image.txt")

if __name__ == "__main__":
    main()