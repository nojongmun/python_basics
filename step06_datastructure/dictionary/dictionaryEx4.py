class Book(object):
    def __init__(self):       # 초기자, 초기화 메서드, 생성자  : 객체 생성
        super(Book, self).__init__()

    def __init__(self, title, author, page):
        super(Book, self).__init__()
        self._title = title
        self._author = author
        self._page = page
    #     self.* =>  인스턴스 변수

    @property   # 속성(변수)에 대한 직접 접근을 차단하는 키워드
    def title(self):    #값을 리턴하는 용도로 사용할 함수
        return self._title

    @property
    def author(self):    #값을 리턴하는 용도로 사용할 함수
        return self._author

    @property
    def page(self):    #값을 리턴하는 용도로 사용할 함수
        return self._page

    @title.setter
    def title(self, value):
        self._title=value

    @author.setter
    def author(self, value):
        self._author=value

    @page.setter
    def page(self, value):
        self._page=value

if __name__ == '__main__':
    bk1 = Book('python', 'kim', '200')
    bk2 = Book('ruby', 'lee', '100')
    bk3 = Book('R', 'park', '300')

    dict_book={bk1.title:bk1, bk2.title:bk2, bk3.title:bk3}

    title=input('찾는 도서를 입력하세요 : ')

    if title in dict_book==None:
        print('찾는 도서가 없어요 ')
    else :
        print(dict_book.get(title).title)
        print(dict_book.get(title).author)
        print(dict_book.get(title).page)

















