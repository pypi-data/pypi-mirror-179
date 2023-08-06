from abc import ABC, abstractmethod


class Pageable(ABC):
    """
    Abstract interface for pagination information.
    """

    @abstractmethod
    def first(self) -> "Pageable":
        """
        Return the :class:`Pageable` requesting the first page.

        :return:
        """
        raise NotImplementedError()

    @abstractmethod
    def has_previous(self) -> bool:
        """
        Returns if there's a previous :class:`Pageable` we can access from the current one. Will return false in
        case the current one already refers to the first page.

        :return:
        """
        raise NotImplementedError()

    def is_paged(self) -> bool:
        """
        Returns whether the current :class:`Pageable` contains pagination information.

        :return:
        """
        return True

    def is_unpaged(self) -> bool:
        """
        Returns whether the current :class:`Pageable` does not contain pagination information.

        :return:
        """
        return not self.is_paged()

    @abstractmethod
    def next(self) -> "Pageable":
        """
        Returns the :class:`Pageable` requesting the next :class:`Page`.

        :return:
        """
        raise NotImplementedError()

    @abstractmethod
    def offset(self) -> int:
        """
        Returns the offset to be taken according to the underlying page and page size.

        :return: the offset to be taken.
        """
        raise NotImplementedError()

    @staticmethod
    def of_size(page_size: int) -> "Pageable":
        """
        Creates a new :class:`Pageable` for the first page (page number 0) given page size.

        :param page_size: the size of the page to be returned, must be greater than 0.
        :return: a new :class:`PageRequest`.
        """
        return PageRequest(page=0, size=page_size)

    @abstractmethod
    def page_number(self) -> int:
        """
        Returns the page to be returned.

        :return: the page to be returned
        :raises NotImplementedError: if the object is unpaged.
        """
        raise NotImplementedError()

    @abstractmethod
    def page_size(self) -> int:
        """
        Returns the number of items to be returned.

        :return: the number of items of that page
        :raises NotImplementedError: if the object is unpaged.
        """
        raise NotImplementedError()

    @abstractmethod
    def previous_or_first(self) -> "Pageable":
        """
        Returns the previous :class:`Pageable` or the first :class:`Pageable` if the current one is already the
        first one.

        :return:
        """
        raise NotImplementedError()

    @staticmethod
    def unpaged() -> "Pageable":
        """
        Creates a :class:`Pageable` instance representing no pagination setup.

        :return:
        """
        return Unpaged()

    @abstractmethod
    def with_page(self, page_number: int) -> "Pageable":
        """
        Creates a new :class:`Pageable` with page number applied.

        :param page_number:
        :return: a new :class:`PageRequest`.
        :raises NotImplementedError: if the object is unpaged and the page number is not zero.
        """
        raise NotImplementedError()


class PageRequest(Pageable):
    """
    Basic implementation of :class:`Pageable`.
    """

    def __init__(self, page: int, size: int):
        """
        Creates a new :class:`PageRequest`. Pages are zero indexed, thus providing 0 for page will return the first
        page.

        :param page: zero-based page index, must not be negative.
        :param size: the size of the page to be returned, must be greater than 0.
        """
        if page < 0:
            raise ValueError("Page index must not be less than zero")
        if size < 1:
            raise ValueError("Page size must not be less than one")
        self.page = page
        self.size = size

    def first(self) -> "PageRequest":
        return PageRequest(page=0, size=self.size)

    def offset(self) -> int:
        return self.page * self.size

    def has_previous(self) -> bool:
        return self.page > 0

    def next(self) -> "PageRequest":
        return PageRequest(page=self.page + 1, size=self.size)

    def page_number(self) -> int:
        return self.page

    def page_size(self) -> int:
        return self.size

    def previous_or_first(self) -> "PageRequest":
        return (
            self if self.page == 0 else PageRequest(page=self.page - 1, size=self.size)
        )

    def with_page(self, page_number: int) -> "PageRequest":
        return PageRequest(page=page_number, size=self.size)


class Unpaged(Pageable):
    """
    :class:`Pageable` implementation to represent the absence of pagination information.
    """

    def first(self) -> "Pageable":
        return self

    def offset(self) -> int:
        raise NotImplementedError()

    def has_previous(self) -> bool:
        return False

    def is_paged(self) -> bool:
        return False

    def next(self) -> "Pageable":
        return self

    def page_number(self) -> int:
        raise NotImplementedError()

    def page_size(self) -> int:
        raise NotImplementedError()

    def previous_or_first(self) -> "Pageable":
        return self

    def with_page(self, page_number: int) -> "Pageable":
        if page_number == 0:
            return self
        raise NotImplementedError()
