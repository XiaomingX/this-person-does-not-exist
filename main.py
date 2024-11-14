import requests
import hashlib
import uuid


def save_picture(picture: bytes, file: str = None) -> int:
    """
    Save a picture to a file. If no filename is provided, generate one using a random hash.
    :param picture: picture content as bytes
    :param file: filename as string (optional)
    :return: int returned by file.write
    """
    if file is None:
        file = uuid.uuid4().hex + ".jpeg"
    with open(file, "wb") as f:
        return f.write(picture)


def get_online_person() -> bytes:
    """
    Get a picture of a fictional person from the ThisPersonDoesNotExist webpage.
    :return: the image as bytes
    """
    response = requests.get("https://thispersondoesnotexist.com", headers={'User-Agent': 'My User Agent 1.0'})
    return response.content


def save_online_person(file: str = None) -> int:
    """
    Get a picture of a fictional person from the ThisPersonDoesNotExist webpage, and save it to a file.
    :param file: filename as string (optional)
    :return: int returned by file.write
    """
    picture = get_online_person()
    return save_picture(picture, file)


def main():
    # Example usage: Save an online person's picture to a file
    bytes_written = save_online_person()
    print(f"Saved {bytes_written} bytes to a randomly generated filename")


if __name__ == "__main__":
    main()
