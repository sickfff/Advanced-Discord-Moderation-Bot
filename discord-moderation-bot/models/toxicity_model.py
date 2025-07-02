from detoxify import Detoxify
import asyncio

class ToxicityModel:
    def __init__(self):
        self.model = Detoxify('original')

    async def predict(self, text: str) -> float:
        # Run model asynchronously
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, lambda: self.model.predict(text))
        # Return max toxicity score among labels
        return max(result.values())
