class Router:

    def route(self, text):

        text = text.strip()
        lower = text.lower()

        if lower.startswith("search google for "):

            query = text[len("search google for "):].strip()

            return {
                "intent": "google_search",
                "query": query
            }

        if lower.startswith("google "):

            query = text[len("google "):].strip()

            return {
                "intent": "google_search",
                "query": query
            }

        if lower.startswith("search for "):

            query = text[len("search for "):].strip()

            return {
                "intent": "google_search",
                "query": query
            }

        if lower.startswith("open "):

            app_name = text[5:].strip()

            return {
                "intent": "open_app",
                "app": app_name
            }

        return {
            "intent": "chat"
        }