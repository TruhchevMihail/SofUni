class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = (photos_count + cls.PHOTOS_PER_PAGE - 1) // cls.PHOTOS_PER_PAGE
        return cls(pages)

    def add_photo(self, label: str):
        for page_index in range(self.pages):
            if len(self.photos[page_index]) < self.PHOTOS_PER_PAGE:
                self.photos[page_index].append(label)
                return f"{label} photo added successfully on page {page_index + 1} slot {len(self.photos[page_index])}"
        return "No more free slots"

    def display(self):
        result = []
        for page in self.photos:
            result.append("-----------")
            if page:
                result.append(" ".join("[]" for _ in page))
            else:
                result.append("")
        result.append("-----------")
        return "\n".join(result)
