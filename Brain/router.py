class Router:

    def route(self, text):

        text = text.strip()

        lower = text.lower()

        if lower.startswith("open "):

            app_name = text[5:].strip()

            return {
                "intent": "open_app",
                "app": app_name
            }

        return {
            "intent": "chat"
        }