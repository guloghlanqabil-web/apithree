class News:

    def __init__(self, tit, des, img):

        self.tit = tit
        self.des = des
        self.img = img

news1 = News(
    "iphone 16 Pro Max",
    "Released in September 2024, the Apple iPhone 16 Pro Max features a massive 6.9-inch Super Retina XDR display, a faster A18 Pro chip, and enhanced 48MP camera capabilities. It offers the longest battery life of any iPhone, lasting up to 33 hours of video playback. It boasts Apple Intelligence, a titanium frame, and Wi-Fi 7.",
    "https://github.com/guloghlanqabil-web/image/blob/main/iphone_16_pro_max.png?raw=true"
)

news2 = News(
    "AirPods Pro 3",
    "The AirPods Pro 3 (2026) are advanced in-ear earbuds offering up to 4x better active noise cancellation than previous models, featuring the H2 chip, heart rate tracking during workouts, and Live Translation capabilities. The AirPods Max 2 (2026) provide over-ear comfort with 1.5x better noise cancellation, longer battery, and USB-C.",
    "https://github.com/guloghlanqabil-web/image/blob/main/Apple-AirPods-Pro-3.jpg?raw=true"
)

news3 = News(
    "Apple Watch Ultra 3",
    "The Apple Watch Ultra 3 is a high-performance smartwatch for fitness and adventure, featuring a 49mm titanium case and a 3,000-nit display with improved angles. It boasts up to 42 hours of battery (72 in low power), improved 1Hz refresh rates, advanced health tracking (Vitals, sleep apnea, blood oxygen), and new black/natural titanium finishes.",
    "https://github.com/guloghlanqabil-web/image/blob/main/Apple-Watch-Ultra-3.jpg?raw=true"
)

news_list = [news1, news2, news3]