class QuoteModel:
    """
    Contains text fields for body and author

    """

    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __str__(self):
        return f'(body:{self.body},author:{self.author})'

    def __repr__(self):
        return f'(body:{self.body},author:{self.author})'
