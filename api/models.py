class News:
    def __init__(self, tit, des, img):

        self.tit = tit
        self.des = des
        self.img = img

news1 = News(
    "Iphone 16 Pro Max",
    "The Apple iPhone 16 Pro Max (released September 2024) is a flagship smartphone featuring a massive 6.9-inch Super Retina XDR display, a durable titanium design, and the powerful A18 Pro chip. It boasts a 48MP Fusion camera system, up to 30 hours of video playback, and supports Apple Intelligence features.",
    "https://github.com/guloghlanqabil-web/image/blob/main/iphone_16_pro_max.png?raw=true"
)
news2 = News(
    "AirPods Pro 3",
    "Apple AirPods Pro 3 (expected 2025) focus on advanced health tracking with built-in heart rate sensors, significantly improved Active Noise Cancellation (2x better than Gen 2), and a more secure fit. They feature a new H2 chip, enhanced spatial audio, IP57 dust/water resistance, and potential AI-driven hearing health features, offering around 8 hours of battery.",
    "https://github.com/guloghlanqabil-web/image/blob/main/Apple-AirPods-Pro-3.jpg?raw=true"
)
news3 = News(
    "Apple Watch Ultra 3",
    "The Apple Watch Ultra 3 (released September 2025) is the most advanced, durable smartwatch from Apple, featuring a 49mm titanium case, the largest display, and up to 42 hours of battery life (72 in Low Power Mode). It offers built-in satellite communications, 5G cellular, and enhanced health tracking including sleep scores, hypertension notifications, and advanced metrics for sports.",
    "https://github.com/guloghlanqabil-web/image/blob/main/Apple-Watch-Ultra-3.jpg?raw=true"
)
news_list = [news1, news2, news3]       