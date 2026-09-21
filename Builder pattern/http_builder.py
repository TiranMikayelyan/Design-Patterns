class HttpRequest:
    def __init__(self, method, url, headers, body):
        self.method = method
        self.url = url
        self.headers = headers
        self.body = body

    def send(self):
        print(f"Method: {self.method}")
        print(f"URL: {self.url}")
        print(f"Headers: {self.headers}")
        print(f"Body: {self.body}")


class HttpRequestBuilder:
    def __init__(self):
        self.method = "GET"
        self.url = ""
        self.headers = {}
        self.body = None

    def set_method(self, method):
        self.method = method
        return self

    def set_url(self, url):
        self.url = url
        return self

    def add_header(self, key, value):
        self.headers[key] = value
        return self

    def set_body(self, body):
        self.body = body
        return self

    def build(self):
        return HttpRequest(
            self.method,
            self.url,
            self.headers,
            self.body
        )


request = (
    HttpRequestBuilder()
    .set_method("POST")
    .set_url("https://api.example.com/users")
    .add_header("Content-Type", "application/json")
    .add_header("Authorization", "Bearer 123")
    .set_body('{"name": "Tiran", "age": 23}')
    .build()
)

request.send()
