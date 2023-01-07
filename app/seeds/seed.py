from app.models import db, User, Product, ProductImage, Review, ReviewImage
from app.seeds.upload import upload_image_to_bucket_from_url


def seed_all():
    demo = User(
        fullname="Demo",
        email="email@email.com",
        password="password"
    )

    seller = User(
        fullname="Seller",
        email="seller@email.com",
        password="password"
    )

    brian = User(
        fullname="Brian Cortez",
        email="brian@email.com",
        password="password"
    )

    caitlynn = User(
        fullname="Caitlynn Rollins",
        email="caitlynn@email.com",
        password="password"
    )

    derrik = User(
        fullname="Derrik Watson",
        email="derrik@email.com",
        password="password"
    )

    elizabeth = User(
        fullname="Elizabeth Bethlehem",
        email="elizabeth@email.com",
        password="password"
    )

    sarah = User(
        fullname="Sarah Armstrong",
        email="sarah@email.com",
        password="password"
    )

    db.session.add(demo)

    # https://www.amazon.com/Philips-Sonicare-Toothbrush-Rechargeable-HX3681/dp/B09LD7WRVS

    product = Product(
        seller=seller,
        title="Philips Sonicare 4100 Power Toothbrush, Rechargeable Electric Toothbrush with Pressure Sensor, Black HX3681/24",
        price="39.99",
        description="Removes up to 5x more plaque vs. a manual toothbrush\nPressure sensor and two intensity settings protect sensitive gums from overbrushing\n2 minute SmarTimer with QuadPacer ensure Dentist-recommended brushing time\nBrush head replacement reminder ensures your brush head is always effective\nLong battery life with battery light indicator: One charge last for 2 weeks\nIncludes: 1 Philips Sonicare 4100 handle, 1 Optimal Plaque Control (C2) brush head, and 1 USB charger (wall adaptor not included)\nSRG, Test Report, CIPS918151 (2021)"
    )

    db.session.add_all([

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/713c7c3UWrL._SL1500_.jpg"),
            preview=True,
            position=1
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71FWv6ibykL._SL1500_.jpg"),
            preview=False,
            position=2
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71IioUiA+ML._SL1500_.jpg"),
            preview=False,
            position=3
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/714wHoGhTfL._SL1500_.jpg"),
            preview=False,
            position=4
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61hwmY1cGTL._SL1500_.jpg"),
            preview=False,
            position=5
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/6180V77bcKL._SL1500_.jpg"),
            preview=False,
            position=6
        ),

        ReviewImage(
            review=Review(
                buyer=brian,
                product=product,
                rating=5.0,
                review="I generally write reviews when products seriously impress me or leave me very disappointed. This Philips Sonicare electric toothbrush did not disappoint. I have always been an analogue tooth brush user, but after this I have been converted.\n\nSome background: this year I started a new health regime and as part of that started drinking *lots* of coffee and tea. However several months in I noticed my teeth started to develop serious staining! This was despite brushing teeth very thoroughly twice a day. Regular brushing did not seem to help with my staining, and as time went by it continued to get worse and worse. I learned that plaque also stains more easily than enamel, and so this served to highlight all of the plaque in my mouth that had been accumulating over time.\n\nI did not want to reduce my coffee and tea consumption, nor did I want to go through abrasive teeth whitening procedures (also that would not solve my apparent plaque issue). After some research, I thought perhaps an electric toothbrush would help, so I bought this Sonicare and have not looked back. I brush twice a day, once in the morning and once at night. I do two cycles per brushing, one according to the instructions that come with the toothbrush, and another immediately after to focus on the more stained regions of my teeth.\n\nFast forward two months, and the stains on my front teeth have almost entirely disappeared! The plaque that had accumulated has also started to go away. I am seriously impressed, and never imagined that an electric toothbrush would have such a profound impact on my dental health! While it may be gross, see my attached photo. The light stain on the front left tooth used to cover over 80% of the surface. Now it is almost gone. My other teeth definitely need some tough love and care, but it is a major step in the right direction. It definitely takes time for the plaque to go away (do not expect magical results overnight), but with patience and proper brushing your oral health will certainly be improved.\n\nAside from the potent cleaning power of this toothbrush, the battery life is excellent, typically lasts me 3-4 weeks before alerting me to a recharge. Additionally it is rather portable, especially when you remove the toothbrush head from the body.\n\nIf you are not using an electric toothbrush, I urge you to make the swap. Your teeth will be so much cleaner. I can't say how my Sonic stacks up against other electric toothbrush brands, but I can say that this model certainly does the job.",
                title="Amazing! Removes coffee / tea stains and plaque!"
            ),
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/51H8iZ1vgwL._SL1500.jpg"),
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5.0,
            review="I have had a few different Sonicare toothbrushes over the past 20 years. I have also tried several other brands of electric toothbrushes.  I have found no brand that meets or exceeds Philips Sonicare toothbrushes.  I bought this pink Sonicare 4100 for my daughter, after she finally called it quits on the other brand electric toothbrush I gave her last year (it had a three sided head that enticed me into buying it…hoping it would improve her thoroughness).  I gave my black 4100 (with a new head) to my husband after my friend gifted me a new Sonicare for gum care. I jones prefer the 4100, but the difference is so minor it really doesn’t matter. I find these 4100 are an excellent choice as far as value and durability and battery life (I can easily pack it for a 10 day trip and leave the charger at home).  In fact, I like to keep the charger in the medicine cabinet and only charge my toothbrush when the battery is almost entirely drained (as opposed to just keeping it on the charger)…I think this may be why I have had such good experiences with these batteries lasting.  The replacement heads are more expensive than I wish, and that to me is the only drawback.",
            title="I LOVE PHILIPS SONICARE TOOTHBRUSHES!"
        ),

        ReviewImage(
            review=Review(
                buyer=derrik,
                product=product,
                rating=5.0,
                review="While it cost a bit more than I wanted to pay, it is a really good toothbrush. I love that it has a timer for 2 minutes, with a beep every 30 seconds so you can time your brushing to each quarter of your mouth. The toothbrush shuts off when the 2 minutes are up. You can shut it off before then or turn it back on if needed but I have found the timer to be very helpful. It has two speeds but I've primarily used the slower one which seems fast enough. When I first used it all the vibrating from that slower speed felt very weird to my mouth and jaw. I'm used to it now though. It charges well. I've noticed that when the battery has died a little bit that maybe the 30 second timers don't beep. It's nice that you can have that warning to charge it rather than it just dying. It's also nice that it comes with a cover for the head of the toothbrush and that it's one that isn't completely sealed so you're not encouraging mold or anything like that. It would have been nice if the charger came with the wall adapter, but as you can see in the pictures, it did not. It's a regular USB plug (and it's not like I'd charge my toothbrush using my computer!) so I had to buy the wall adapter separately.",
                title="Good toothbrush with some nice features"
            ),
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/717lvVnMouL._SL1500.jpg"),
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5.0,
            review="I’ve had this for two weeks and love it. I was lucky enough to buy it on a Cyber Monday deal so got a great price to boot! It has a timer for each quadrant of your teeth (upper outside, lower outside, lower inside, and upper inside), that helps ensure a good brushing time. It also has an over pressure sensor so you don’t press to hard, and it shuts off when your brush time is done. It comes with one brush head and will signal when the head is worn down, so I set up a replacement service through Amazon’s subscribe and save. It needs to be noted that the instructions state the sensors only work with genuine Sonicare replacement heads. That, and the face that it does not come with a travel case ( though you can order one reasonably) are the only cons for this toothbrush.",
            title="Geez, I should have done this years ago!"
        ),

        Review(
            buyer=sarah,
            product=product,
            rating=5.0,
            review="I looked at reviews and most importantly, the U-Tube reviews on current electric toothbrushes.\n(The 'Electric Dentist' U-Tube ones are the most credible ones.}\n*I'm delighted with this product having used it now for about 4 weeks. What i find most appealing is that it has a very slim, natural feel in your hand!  Also, the bush head is smaller, so (in my mouth) it's much easier to get to my wisdom teeth and minimizes that so annoying e 'gagging' I've had with other units. I like its 2-speed power design also. I can honestly say, it's the very best and most effective toothbrush I have ever owned, and I have owned many over the years.",
            title="The Best ultrasonic toothbrush!"
        ),
    ])

    # https://www.amazon.com/AquaSonic-DUO-Whitening-Rechargeable-ToothBrushes/dp/B07HFG93GK/ref=sr_1_16?crid=234FOMCTX8NL8&keywords=electric+toothbrushes&qid=1673123804&s=hpc&sprefix=electric+toothbrushes%2Chpc%2C286&sr=1-16

    product = Product(
        seller=seller,
        title="Aquasonic Duo - Dual Handle Ultra Whitening 40,000 VPM Wireless Charging Electric ToothBrushes - 3 Modes with Smart Timers - 10 Dupont Brush Heads & 2 Travel Cases Included",
        price="49.95",
        description="Complete Oral Care for 2 – AquaSonic Duo provides complete oral care in one simple countertop setup. Duo features 2 modern smart toothbrushes with the latest oral care technologies including 40,000 vibration per minute motors, true wireless charging, 3 unique modes including modes for whitening teeth and gum health, 30-day battery life, in sleek midnight black and optic white brush handles. Duo Series comes with 12 additional accessories including 10 DuPont brush heads and 2 travel cases.\nModern Technology For A Healthier Smile - Each Duo toothbrush bring your oral health routine into modern times with its built in enhanced features. Super fast wireless charging, 3 distinct brushing modes and a smart vibrating notification timer are some of the enhanced features built in to the sleek and ergonomic waterproof black and white satin handles.\nConvenient Modern Home & Travel Set-Up – Duo is perfect for couples, kids or anyone in between. A simple dual wireless charging dock takes up a few inches of countertop space while adding a sleek modern element to your bathroom. Duo’s 30 day battery life means it’s also perfect for travel – simply put your duo in its included travel case and take it on the go while leaving the charger at home.\nAll The Extras; Already Included - Every DUO set comes with 10 brush heads engineered by world famous DuPont; a world leader in quality & materials science. Also included are 2 convenient color coded custom hard shell travel case made of BPA Free plastic with space for two brush heads. No need to buy expensive brush head refills or extra accessories. It’s already in the box.\nWhat's Included - 1 Midnight Black Smart Toothbrush, 1 Optic White Smart Toothbrush, 1 Dual Wireless Charging Dock, 2 Travel Cases, 10 DuPont Brush Heads, Support & Warranty Manuals."
    )

    db.session.add_all([

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/7117K2Ej9AS._SL1500_.jpg"),
            preview=True,
            position=1
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/514JKoE2ORL._SL1500_.jpg"),
            preview=False,
            position=2
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61TeEKfTfAL._SL1500_.jpg"),
            preview=False,
            position=3
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71br2SZvuDL._SL1500_.jpg"),
            preview=False,
            position=4
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61moFmMBS-L._SL1500_.jpg"),
            preview=False,
            position=5
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/814N7D60dAL._SL1500_.jpg"),
            preview=False,
            position=6
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5.0,
            review="First let me say that this is my second time purchasing this brand. This is an excellent brand brushes and cleans teeth very well. I love and uses all three features on the brush. I bought this toothbrush for me and my husband, however my brush stopped working after 3years of  use would not charge even after having it on charger for weeks but my husband toothbrush was still work even onto this day. I could not tolerate using regular tooth brush anymore so I decided to purchase another set again. I am hoping that this one will continue to work for much longer time than previous purchase. I definitely will recommend this brand to my family and friends",
            title="Brushes great teeth are clean and sparkly."
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5.0,
            review="Brushing: Really good clean. The 3 modes do as advertised. Must be kept close to fully charged to give that real clean feel though.  The timer works well.\nUnit: Seems like a stong design since I've been using for a year. I read the other reviews about some persons noticing the end of the head unit being left on the handle. So, whenever I am detaching I get a grip (or place  a nail under the joining) to hold it in place. No separation yet. The silver parts of the unit are decoration and they will flake and come off. That does not affect the brusing.\nPresentation: The case is sturdy. One takes a bit of muscle to open. Really good for travelling.\nBut: would have liked a bristle cover for when it is on the charging stand",
            title="Decent Brush"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5.0,
            review="I will say these are great toothbrushes that actually leave your teeth feeling clean and smooth. However I don’t like how rough they are at first. My gums are pretty sore and I wish they were like my last toothbrush and had a sensitive mode on them. I’ll get used to it eventually. I also didn’t like that I couldn’t take it out of my mouth to spit because when I did, toothpaste flung everywhere due to the power of it.",
            title="Little rough at first"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5.0,
            review="I bought one of these maybe a year ago and they are great toothbrushes.  I have always bought oral B tooth brushes and I think these are better.  They really get your teeth clean and give a thorough massage to your gums.  my teeth feel cleaner at night before I brush at bedtime.  My husband and I shared one but now we each have our own brush and handle.  We are pleased",
            title="What a GREAT buy"
        ),

        Review(
            buyer=sarah,
            product=product,
            rating=5.0,
            review="Love the toothbrushes.  Comes with several extras, nice travel case.  The battery seems to last a really long time.  The timer feature is really nice.  Didn't realize that we didn't brush a full two minutes!  My teeth feel clean and the gum feature feels great.  I would recommend this product.  Great value.",
            title="Awesome Purchase"
        ),
    ])

    # https://www.amazon.com/Oral-B-iO-Electric-Toothbrush-Rechargeable/dp/B0B5HTX7YW/ref=sr_1_11?crid=234FOMCTX8NL8&keywords=electric%2Btoothbrushes&qid=1673124949&s=hpc&sprefix=electric%2Btoothbrushes%2Chpc%2C286&sr=1-11&th=1

    product = Product(
        seller=seller,
        title="Oral-B iO Series 4 Electric Toothbrush with (1) Brush Head, Rechargeable, White",
        price="79.97",
        description="You will receive (1) Oral-B iO4 Electric Toothbrush, (1) Ultimate Clean Replacement Brush Head, and (1) Travel Case, and (1) charger\nClinically proven to remove 500% more plaque along the gumline vs. a regular manual toothbrush\n4 Smart Modes for personalized brushing: Daily Clean, Whiten, Sensitive, and Super Sensitive\nIncludes a 2 minute timer to ensure a complete clean\nPressure sensor indicates optimal cleaning pressure and warns of over pressure\nRound head and gentle micro-vibrations\nOral-B: Trust the brush dentists use the most worldwide"
    )

    db.session.add_all([

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/711-QghlPoL._SL1500_.jpg"),
            preview=True,
            position=1
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71JynsevysL._SL1500_.jpg"),
            preview=False,
            position=2
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/614VD8tZ5pL._SL1500_.jpg"),
            preview=False,
            position=3
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61pgRoDqg2L._SL1500_.jpg"),
            preview=False,
            position=4
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71P4C1SrM1L._SL1500_.jpg"),
            preview=False,
            position=5
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/613znQzOUnL._SL1500_.jpg"),
            preview=False,
            position=6
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5.0,
            review="I finally broke down and decided to get an electric toothbrush after a recent dentist visit. I drink a lot of herbal teas and concoctions for various health reasons, so staining is an unwelcomed problem. Having missed my previous 6-month cleaning due to having COVID, I was close to the 1-year mark when I sat down in the dentist's chair. I saw seen by a new dental hygienist who showed me how bad the staining was behind my upper front teeth and mentioned that she too has some issues with dark stains, so it is not uncommon. However, when the dentist came to examine it, she indicated that it was not staining and recently discovered at a conference that although this appeared to be a stain, it is actually harmful bacteria that would require treatment with antibiotics and deep cleaning. I begged to different as I explained that I drink herbal teas and always have the same staining issues, but she insisted and said that I would need to come back for deep cleaning over 2 days. I asked her if the insurance company would cover it. She laughed and said that's between you and your insurance company, I don't get involved in that. I explained to her that I had the same thing happen many years ago and ended up paying out of pocket ($1200) because the insurance company said the deep cleaning was unnecessary. As she walked out, she proclaimed that this looks like five years of growth.\n\nThe hygienist looked at me after she left and asked, how long have you been coming here? I said 5 - years, she asked if that was the dentist who I usually see and I said no. This is only the second time she examined me; in fact, she was the dentist who examined me at my last cleaning less than one year ago. She said, so if this took 5 years to build up, why didn't she notice it? I told her that is exactly what I wanted to say to her when she said that, but she was walking out as she said it.\n\nFast forward -\n\nI purchased this toothbrush at the recommendation of the hygienist and low and behold, 95% of the stains were removed on the first use. This is a powerful toothbrush and the fact that it is round, makes a huge difference in getting at the plaque under the base of the gums.\n\nMost dentists are using every tactic to charge more money. Her office now does Botox, laser hair removal, etc., and I get flyers and post cards from other area dentists who are doing this as well. So it did not surprise me when she insisted that I required deep cleaning, which is why I asked the insurance question since I've been down that road before. When they did the number system to determine how deep the pockets were, I had mostly 2s and 3s. The 4s that were initially indicated were dismissed as 3s when the dentist came to exam me until she noticed the staining behind the upper teeth and then suddenly, I needed deep cleaning.\n\nBottom line, this is a powerful toothbrush. I scraped the stains as much as I could, and manually brushed to no avail with a HARD Colegate toothbrush, but as soon as I used the IO4, the stains were nearly completely gone.  Having used this toothbrush for the past several weeks, the sensitivity and minor gum pains that have been present for quite some time, have all but disappeared. The bristles of the brush stimulate the gums, and breach the gumline, helping to remove plaque buildup, which explains the disappearing pain.\n\nAs for the 4 modes, I only notice a slight difference between them, but usually use it on the initial setting which is for daily brushing. Cost is high on these, so I recommend shopping around and checking the Oral B website for sales. I got this from Amazon when they were at $59, but nearly missed the sale. I placed it in my car the night before and forgot to complete the transaction. The next morning it was back to $99. I quickly checked the other colors and found white still showing $59.  After few moments after I bought it, it was up to $99. I guess the price adjustments had not been completed, otherwise I would not have bought it although it's probably worth it.  Obviously, I'm cancelling the deep cleaning and will likely find a new dentist for the exact same reason why I left the other office. I'm not accusing her trying to cheat me, but had I not bought this toothbrush, I'd be paying out of pocket for another deep cleaning I did not need.\nGreat powerful toothbrush... No, you don't need all these fancy modes that are just marketing spin to get you to pay a higher price. Oral B's lower priced models are probably just as powerful.\n\nYMMV\n\nYMMV",
            title="Powerful toothbrush"
        ),

        ReviewImage(
            review=Review(
                buyer=caitlynn,
                product=product,
                rating=4.0,
                review="I haven’t used an electric brush in years so they have come a long way with the fact of adding Bluetooth to the device. I have been using just manual tooth brushes for years and they seem to do the job moderately so hopefully this will be a step in the right direction to better and healthier oral care.\n\nPackaging: The box and the design are great and appealing. You are able to understand what features are offered with the toothbrush. The box recyclable and I would recommend that everyone do so to help the environment. With how big the company Oral-B is and the price of the product I would expect the design and graphics to look top notch.\nUpon opening the contents are securely held in a molded piece of Styrofoam. Other parts such as the charger were securely held together with cardboard. With this much packaging less likely anything will be destroyed while shipping.\n\nAppearance: At first it looks like there are a lot of parts to this, but once it’s all assembled it really isn’t that much.\nThe stand arrives in two pieces. It’s easy to assemble and looks sleek and stylish with the white and grey colors for any bathroom countertop. I really like the fact that both the bottom of the tooth brush and top of the charger are completely covered in plastic that is easy to wipe clean. Whereas my past electronic tooth brushes there was plenty of nooks and crevices for stuff to build up.\nThe feel of the tooth brush was a lot chunkier and heavier than the manual tooth brushes that I use.  Not to say it’s not ergonomic to fit your hand well just need to get used to the feel of it. The power switch is easily accessible for your thumb to turn on and off. Even though it’s easily accessible the pressure needed to turn on and off is a bit much. Plus you have to go through the modes until you turn it off.\nI should note I am left handed and this feels comfortable in my hand. This is nice because it’s at least one product that is made for both left and right handers.\nThe brush head moves like a kit-cat clocks tail from left to right with the push of your fingers. The feel of the bristles are strong, durable and flexible as well. It’s easy to install the brush head and clicks securely onto the tooth brush. Takes tiny pressure and is just as easy to remove.\nThe charger easily clicks into the stand and looks good as one entire piece. The stand also holds extra brush heads under a little cover to keep everything clean for the most part while providing ventilation for the brush heads to dry out. If you don’t want to use the stand you can use the charging port alone.\nI think the charging cord is a good length, I roughly measured 45 inches. For me my bathroom counter is small and so I keep most of the cord wrapped up. I ended storing the charging station/stand because I already have a place for the toothbrush. I do bring it out when I need to charge.\nI really like the fact the brushes battery lasts for 7 days with 2 minutes twice a day that way if you get in a pattern like I have you only have to charge it Sunday night. It says it can take up to 22 hours to charge. The unit flashes green light to let you know it’s charging and turns off once it’s completely charged. If you are using the brush and the battery is low the red charger signal turns under the battery light.\n\nUse:  After using this for about a month I am beyond satisfied that I had the opportunity to use this toothbrush. The benefits are so much more worth the manual. The best part is being reminded by the signal to switch quadrants compared to before where I was just doing it haphazardly. I also like the signal letting me know I am apply too much pressure while brushing. That has been a definite eye opener.\nAs for the app it’s relevant for today’s electronics and I love seeing how I have been doing over the time. It tracks your sessions as long as your phones Bluetooth is on, connected and near your brush. You can also set as schedule focused on particular things like whitening your teeth, gum health and others and they call this your “Journey”. Once you have set this it becomes your personalized journey where you can select targeted problem areas. I think the app is a unique feature and helps you keep up on your oral health.\nI have gotten used to the feel of the vibration and weight of the tooth brush. As monotonous brushing your teeth can be this brush makes it easier and more exciting.\nThe lights on the device are bright but don’t affect me. I like the fact that you can see what you are doing if you are in a dim lit bathroom.\nI can noticeably see a difference in my gum health and the appearance of my teeth. Definitely feel like I accomplish more with this brush than the manual brush.\n\nPrice: A 100 dollar electronic tooth brush is a lot of money to spend compared to using manual tooth brushes. I think that is mainly the reason I avoided going to electronic because the cost of them. I think it would be easier for people to move to such a brush if the price wasn’t so high. I do think it’s a great quality and it does what’s intended.\n\nOverall:  I am very happy with the tooth brush and glad I have crossed over back to the electronic side of brushing teeth. The brush works great and is easy to clean, charge and work with. I think if I had to point out any flaw with the brush it it’s very loud. It almost sounds like a drill.  Also the pressure in which you need to cycle through the modes and turn off it could be a lot easier.\nMine has yet to lose its charge or have battery issues. I will update accordingly. I would cation over charging the battery, over 22 hours I think would damage the battery and it’s longevity.\n\nI received this item at a discounted price for my honest review. Every review I do is based 100% off of my experience with the product and I do not guarantee a positive review.\n\n",
                title="Works great. Signals help you get the best care of your teeth. A little too loud for me."
            ),
            url=upload_image_to_bucket_from_url(
                "https://images-na.ssl-images-amazon.com/images/W/WEBP_402378-T1/images/I/61-65ItjXKL._SL1500.jpg"),
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5.0,
            review="Have two working brushes 15+ Years old. But, I wanted a new brush. Seems stronger than my Triumph brushes. I have great dentist reports. Been using Oral b since way back when the best you could get was Oral b 40, a manual toothbrush. If the battery lasts longer than my Triumphs, this is a great brush. Reviews say the battery goes dead in a year, we’ll see. Love this brush right now.",
            title="Oral b 3000"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5.0,
            review="First thing that hit me about this brush is the power. I’ve used a few cheap electric brushes and never expected the difference to be so extreme. This one actually feels like it’s cleaning. Second thing I like is the app/timer. The brush lets you know by pulses every 30s with more pulses for the 2min mark but the app shows the timer and then asks if you had gum bleeding (I did the first 2 times) then it reminds you to brush your tongue, floss, and rinse with mouthwash. The flossing reminder actually got me to floss more often. Overall I think this brush actually helped me improve my brushing and flossing habits.",
            title="Forms good habits"
        ),

        Review(
            buyer=sarah,
            product=product,
            rating=4.0,
            review="This brush seems to be pretty powerful, has all the basic features you want plus bluetooth.\n\nThe bluetooth app may seem a bit gimmicky but you can register your toothbrush and it tells you what modes are set up for your toothbrush - which is important since the instructions contradicts itself.\n\nThe modes out of the box are:\nDaily --&gt; Sensitive --&gt; Polish\n\nWith the app you can make Sensitive the default mode for example.\n\nCleaning - only started using it but it seems to be pretty good.  The weird thing is, the toothbrush does not auto shutoff after 2min. It just buzzes and keeps on going.. whether you find that annoying or great is up to you... doesn’t seem to be changeable via the app either.\n\nYou can set up the toothbrush on just the little charger stand, or attach it to the larger brush case. The instructions say to remove the brush head after each use and rinse inside/out - but no one is going to be doing that.",
            title="Pretty good with a few quibbles"
        ),
    ])

    # https://www.amazon.com/Colgate-Advanced-Floss-Tip-Vibrating-Toothbrush/dp/B0787G4D3Q/ref=sr_1_10?crid=234FOMCTX8NL8&keywords=electric+toothbrushes&qid=1673124949&s=hpc&sprefix=electric+toothbrushes%2Chpc%2C286&sr=1-10

    product = Product(
        seller=seller,
        title="Colgate 360 Sonic Battery Power Electric Toothbrush with Floss-Tip Bristles, Tongue and Cheek Cleaner, Soft - 2 Count (Pack of 1)",
        price="9.96",
        description="The Colgate Advanced Floss Tip** power toothbrush brushes your teeth easily with only a press of a button\nThe floss-tip**, soft bristles gently reach 4X* deeper below the gumline.\nA cheek, mouth and gum cleaner comfortably removes bad breath bacteria.\n1 AAA battery is included with this single pack designed with sonic vibrations toothbrush.\nEnjoy a whole mouth clean with every brush from this battery powered toothbrush."
    )

    db.session.add_all([

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/7100USN68eL._SY741_.jpg"),
            preview=True,
            position=1
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/51Tv9FWsvnL._SL1500_.jpg"),
            preview=False,
            position=2
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71PKy95DZOL._SY879_.jpg"),
            preview=False,
            position=3
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61PlNOhZVOL._SY879_.jpg"),
            preview=False,
            position=4
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61bTqTeKh-L._SY879_.jpg"),
            preview=False,
            position=5
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5.0,
            review="It’s very different than my plug in oral b toothbrush, but much smaller and easy to pack for travel. It seems to do a good job at  cleaning and is much better than my manual travel brush alternative. I used it for a recent 8 day trip and the battery was fine.",
            title="Very pleased for my travel toothbrush"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5.0,
            review="I bought this toothbrush on sale and I'm happy I did. The battery life lasts longer, and since I started using this toothbrush, I have gotten a good report from the dentist.  Very impressive.",
            title="Very Good Toothbrush"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5.0,
            review="I’ve been using this model for one and a half year. It’s perfect for my sensitive gums.\nReplacing the toothbrush every 3-4 months as usual. New battery every ~2 months.",
            title="Good"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5.0,
            review="Guaranteed your brush will wear out before the battery does. Cleans great and the vibration helps like an electric toothbrush but cheaper and can clean more than one tooth at a time.",
            title="Love these toothbrushes"
        ),

        Review(
            buyer=sarah,
            product=product,
            rating=5.0,
            review="They make my teeth fill very clean and like I just got a cleaning.",
            title="Works well."
        ),
    ])

    # https://www.amazon.com/AquaSonic-Ultra-Whitening-Electric-Toothbrush/dp/B07R8WGDKF/ref=sr_1_23?crid=234FOMCTX8NL8&keywords=electric+toothbrushes&qid=1673124949&s=hpc&sprefix=electric+toothbrushes%2Chpc%2C286&sr=1-23

    product = Product(
        seller=seller,
        title="Aquasonic Vibe Series Ultra Whitening Toothbrush – ADA Accepted Power Toothbrush - 8 Brush Heads & Travel Case – 40,000 VPM Motor & Wireless Charging - 4 Modes w Smart Timer – Satin Rose Gold",
        price="39.95",
        description="40,000 VPM Smart Toothbrush – Beauty, brains and power. The Vibe Series is a world class modern electric toothbrush packed with the most up to date technology. It features an ultra-powerful and industry leading motor producing 40,000 vibrations per minute , lithium-ion battery, ultra-fast wireless charging, 4 mode operation, smart vibration timers, 8 DuPont engineered brush heads, and a custom travel case; all with a sleek, ultra-slim, lightweight and IPX7 rated waterproof body.\nAccepted by the American Dental Association (ADA) Council on Scientific Affairs – We put our money where your mouth is. Investing in premium oral care technologies has earned the Vibe Series the prestigious ADA seal of approval. It has shown efficacy in removing plaque and helping to prevent and reduce gingivitis. Vibe Series goes beyond just cleaning teeth – it provides complete oral care with unique modes that include one for whitening and polishing teeth and one for improving gum health.\n8 DuPont Brush Heads & Travel Case Included - Every Vibe Series toothbrush comes with 8 brush heads engineered by world famous DuPont; a world leader in quality & materials science. Each brush head lasts 4 months so 8 will last for over 2.5 years. Also included is a convenient custom hard shell travel case made of BPA Free plastic with space for two brush heads. AquaSonic can last 4 full weeks (2 min/2x a day) on a full charge so its perfect for on the go travel with the included travel case.\nModern Tech For Complete Oral Care - The Vibe Series brings toothbrushes into modern times with its built in enhanced features. Ultra fast wireless charging (forget cheap USB charging), 4 distinct brushing modes and a smart vibrating notification timer are some of the enhanced features built in to the sleek waterproof and stunningly beautiful satin rose gold handle.\nWhat's in the Box – 1 Satin Rose Gold Smart Toothbrush, 8 DuPont brush heads, 1 custom travel case, Instruction manual, Warranty and support contact manuals."
    )

    db.session.add_all([

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/612kEjKGoeL._SL1500_.jpg"),
            preview=True,
            position=1
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61qOCxVaz5L._SL1500_.jpg"),
            preview=False,
            position=2
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/612jamVHp0L._SL1500_.jpg"),
            preview=False,
            position=3
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71L-Jh0XLwL._SL1500_.jpg"),
            preview=False,
            position=4
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/712T3Pjv2HL._SL1500_.jpg"),
            preview=False,
            position=5
        ),

        Review(
            buyer=brian,
            product=product,
            rating=4.0,
            review="I love this in rose gold. It's more sophisticated and has more features than the sonic electric toothbrush I used to use. The only thing I don't like about it is the placement of the buttons to turn it off and on and change speeds. Right where my thumb wants to rest while I'm using it, so I inadvertently press it numerous times. The sonic toothbrush had the same thing I think that's where they got it from. Bad move to copy that design feature, otherwise I would've given it 5 stars. Very generous provision of extra toothbrushes tho.",
            title="This toothbrush is impressive"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5.0,
            review="I received this on Aug 28th, today Dec 28, I finally saw the red flashing light come my to charge it. I did not charge it when I first got it, so it lasts for quite some time on a full charge. It didn't slow down or malfunction while using it ever. I'm glad I bought this with the case and extra brushes. Super convenient!",
            title="Great Battery Life"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5.0,
            review="This toothbrush is awesome. You’ll be amazed, especially for the price. I’ve always had Sonicare toothbrushes, and I always broke them, and they are so expensive I couldn’t do it again. So I tried this toothbrush, I don’t know if it’s going to last longer, but it works much better. It’s also so much cheaper that I don’t worry about it. It really works so much better. AAA+++",
            title="Awesome!!!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5.0,
            review="I like everything about my new Aquasonic tooth brush.  Because of Covid and a few other things, I'd gotten behind on my dental visits.  My teeth really needed some attention.  This gets into the hard to reach areas and cleans them up!  The unit comes with many extra brushes so there's one for everybody.  It has a one year warranty...and lots of positive reviews.  I'm thinking it's every bit as good as those more expensive brands.  Give it a try!",
            title="Just got it...I really like it. My teeth feel big time clean after only a couple uses!"
        ),

        Review(
            buyer=sarah,
            product=product,
            rating=5.0,
            review="I couldn't answer about the battery because I just plugged it in for a bit and tried it out.  I do like the different settings.  The travel case makes it easy to take along with me.",
            title="Works great!"
        ),
    ])

    # https://www.amazon.com/Oral-B-Pro-Health-Clinical-Battery-Toothbrush/dp/B002HWS9FW/ref=sr_1_24?crid=234FOMCTX8NL8&keywords=electric+toothbrushes&qid=1673124949&s=hpc&sprefix=electric+toothbrushes%2Chpc%2C286&sr=1-24

    product = Product(
        seller=seller,
        title="Oral-B Pro-Health Clinical Battery Power Electric Toothbrush (Colors May Vary)",
        price="15.97",
        description="Oral-B AA Battery powered toothbrush with replaceable brush heads reaches deep to remove plaque between teeth. (Batteries included)\nPrecision clean brush head delivers a dentist inspired tooth-by-tooth cleaning\nConsistent battery performance\nAlso try your Oral-B Pro-Health Clinical Battery Brush with other Oral-B Replacement Brush Heads: CrossAction, Sensitive Gum Care, FlossAction, 3D White\nOral-B is the #1 dentist-recommended toothbrush brand worldwide"
    )

    db.session.add_all([

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/81VFwzrqpqL._SL1500_.jpg"),
            preview=True,
            position=1
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71ZB9sZWZ3L._SL1500_.jpg"),
            preview=False,
            position=2
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/81wn8G+LvfL._SL1500_.jpg"),
            preview=False,
            position=3
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/81nytLQ7d1L._SL1500_.jpg"),
            preview=False,
            position=4
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/81jZutlMJYL._SL1500_.jpg"),
            preview=False,
            position=5
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/81X1y0HY5aL._SL1500_.jpg"),
            preview=False,
            position=6
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5.0,
            review="This electric toothbrush checks all the boxes. It is so simple to operate (2 AA batteries that last a long time) with no charging station to carry around or worry about. When I travel, it is super simple to take it with me and if I forget the batteries, then AA batteries are cheap and sold everywhere throughout the world. It costs a lot less than so many other 'rechargeable' electric toothbrushes and I have never understood why I need to spend $100 or even $50 for a toothbrush. I had an earlier version of this toothbrush from 15 years ago that finally broke down this year and I had paid less than $10 for it - that's great value. I have been using this new electric toothbrush for a few months now and I am very happy that I decided against spending big bucks on the top-of-the-line rechargeable models.",
            title="Amazing value and convenience"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=4.0,
            review="Bought these because we didn't want to take our expensive Oral-Bs while traveling.  These use the exact same heads as our home Oral B Pro toothbrush, so that's a big plus.  But the battery power just isn't the same.  It's gets your teeth clean but forget about deep cleaning.  My wife liked hers so much that she still uses it daily now instead of the more powerful Oral-B Pro.  These are probably the perfect starter brush for kids too.  I bought the 3 pack.  Each brush comes with a head, motor, and batteries.  Add toothpaste and you're ready to go.",
            title="Perfect for travel."
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=4.0,
            review="Replaced an older unit that stopped working. Very satisfied with how the new one works. Not surprised about how it works. Time auto time has a longer “time setting “ on it. Not an issue. Just different.",
            title="Cleaning action. Works as expected."
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=4.0,
            review="I didn't look closely enough to realize this was a battery operated version of the Oral B toothbrush. That means it doesn't have the 'oomph' or rate of rotation of the Oral B I have used for years. My fault. I passed this on to a family member and bought an Oral B Pro 1000 instead, which I LOVE. Worth every penny.",
            title="Should have realized it was just battery operated"
        ),

        Review(
            buyer=sarah,
            product=product,
            rating=4.0,
            review="The first thing I notice about it how powerful it is and at this time I do not know how long the battery will last.  I hope to get many years of usage out of it.",
            title="Powerful"
        ),
    ])

    # https://www.amazon.com/Philips-Sonicare-ProtectiveClean-Rechargeable-HX6423/dp/B084TM4XKG/ref=sr_1_9?crid=234FOMCTX8NL8&keywords=electric+toothbrushes&qid=1673125156&s=hpc&sprefix=electric+toothbrushes%2Chpc%2C286&sr=1-9

    product = Product(
        seller=seller,
        title="Philips Sonicare ProtectiveClean 5300 Rechargeable Electric Power Toothbrush, Black, HX6423/34",
        price="99.96",
        description="Customize your experience with the three different modes: Clean, White and Gum Care.\nPressure sensor protects teeth and gums from excess brushing pressure while improving your gum health up to 100% more vs a manual toothbrush.\nAlways know when to replace your brush head for an effective clean with BrushSync replacement reminder.\n2 minute timer with QuadPacer helps ensure dental professional recommended brushing time and encourages brushing in each quadrant of the mouth.\nBattery indicator light let's you know when to recharge; 2 week battery life. Includes: 1 Philips Sonicare 5300 handle, 1 charger, 1 G2 Optimal Gum Care brush head, 1 travel case, 2 extra W DiamondClean brush heads"
    )

    db.session.add_all([

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/81e58wQ0DrL._SL1500_.jpg"),
            preview=True,
            position=1
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/710xhsvmQtL._SL1500_.jpg"),
            preview=False,
            position=2
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61Pblimu6dL._SL1500_.jpg"),
            preview=False,
            position=3
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71LItfeU4tL._SL1500_.jpg"),
            preview=False,
            position=4
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71bAvAOeI6L._SL1500_.jpg"),
            preview=False,
            position=5
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71DbTUkio9L._SL1500_.jpg"),
            preview=False,
            position=6
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5.0,
            review="I purchased this to replace the previous model that I used for many years.  This model is lighter than the previous one, slightly slimmer,  smoother feeling, and has 3 programs rather than one.  It also has a new feature that I found fascinating.  It sends a unique vibration warning if you push too hard on your gums. This was extremely cool.  I’ve actually been told I press too hard by my dentist.  He said, “It’s a Sonicare.  You don’t have to press hard.  It does the work.”  This new feature really helps me understand the correct pressure to apply.  Highly recommended.",
            title="Lighter, more powerful, more advanced than its predecessor"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5.0,
            review="My teeth have never felt so clean after brushing. This brush works extremely well. My dentist recommended it, and I can see why. Battery life is great. No issues with functionality.",
            title="Love it"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5.0,
            review="The color of the free brushes should go together with the color of the unit.\n\nWiithin the 2 minutes brushing time, it will signal you to change the brushing area of your mouth.",
            title="Balance Clean"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=4.0,
            review="This low-end Sonicare model works as expected.  The more expensive models vibrate stronger but none of them last as long as they should and I would not recommend paying more for when an upgraded model, even thou they are slightly better, when they are not going to last. This is my seventh Sonicare purchase and I have loved them all they just don't hold up. My last model was the top-of-the-line Philips Sonicare. Had it replaced under warranty and the replacement lasted just as long, just under a year. Love the product, they just don't hold up.",
            title="The more expensive models vibrate stronger but none of them last as long they should"
        ),

        Review(
            buyer=sarah,
            product=product,
            rating=5.0,
            review="I am sorry I waited so long to buy a new toothbrush. This is excellent, I highly recommend it. I used a battery powered Phillips toothbrush for the years, it finally died and I had to make a decision on a new toothbrush. I  was hesitant to buy one that requires charging versus battery. Don’t wait, don’t hesitate, this is totally worth it!",
            title="Great product!!!"
        ),
    ])

    # https://www.amazon.com/Philips-Sonicare-Rechargeable-Toothbrush-Shimmer/dp/B09B1C9L85/ref=sr_1_30?crid=234FOMCTX8NL8&keywords=electric%2Btoothbrushes&qid=1673125158&s=hpc&sprefix=electric%2Btoothbrushes%2Chpc%2C286&sr=1-30&th=1

    product = Product(
        seller=seller,
        title="Philips One by Sonicare Rechargeable Toothbrush, Shimmer, HY1200/05",
        price="25.96",
        description="Designed with you in mind, Philips One is a big step up from manual brushing. Battery life up to 30 days\nMicro vibrations and tapered bristles made of soft nylon gently polish teeth for a brighter smile\nTake your manual brushing experience to the next level by pairing regular brush motions with bristle micro-vibrations\n2 Minute Timer with 30 second notifications\nDentists recommend replacing brush heads every 3 months\nThe One is made to travel so you can get that clean feeling any place. It’s sleek and lightweight and fits neatly into a compact travel case\nBrush heads match colorful handle for super sleek look. Handles are ONLY compatible with Philips One brush heads. Includes: One (1) Philips One by Sonicare Rechargeable Toothbrush and matching brush head; 1 travel case; 1 USB charger"
    )

    db.session.add_all([

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71uOqpP+B7L._SL1500_.jpg"),
            preview=True,
            position=1
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71iNMTjzlyL._SL1500_.jpg"),
            preview=False,
            position=2
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61drzmS4MBL._SL1500_.jpg"),
            preview=False,
            position=3
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71H0sis5USL._SL1500_.jpg"),
            preview=False,
            position=4
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5.0,
            review="Writing this as a former dental professional. (this by no means makes me an expert) I was a huge fan of the OralB Pulsonic. It was a small, portable effective brush with all the bells and whistles of the bigger brushes. When mine finally died after 10+ years i came to find that brush was discontinued. After an exhaustive search, this was the only rechargeable portable brush i could find that i felt could be a decent replacement. It honestly was better than i expected. It was so inexpensive i feared it would be junk; it is not! The small size is perfect for my everyday and travel needs; the fact that it can be charged with a phone charger is a bonus and i love the travel case that also helps keep the brush drawer clean. More importantly, the brush head is wonderful! I was used to the round brush heads with the previous brand i used, which is pretty great at getting all the tooth surfaces. The Philip's brush heads are shaped like a regular toothbrush, but are so much softer than what i was using before. People don't realize how much damage hard bristles can do to one's gums if you aren't a gentle brusher. It's the reason other sonic brushes have a flashing red light feature to let you know when you're using too much pressure. The 2 minute timer with 30 second and one minute prompts are exactly like what i was used to as well. Been using it for close to a month now and haven't needed to recharge yet. The soft brush head is also holding up. It's not as powerful as other brushes, but unless you have a ton of plaque or stain, (no judgement) this is should do the job and is a steal for under $20",
            title="under rated"
        ),

        ReviewImage(
            review=Review(
                buyer=caitlynn,
                product=product,
                rating=5.0,
                review="I’ve been using this toothbrush for a little over a year now (purchased Dec. 3, 2021) and have had very little issue with it. However, this morning I smelled something burning and found that it was the toothbrush that I had plugged in a couple hours before to charge. Everything including the toothbrush and the cord was hot to touch and part of the toothbrush melted off and stuck to the usb port. Thankfully I work from home so I was able to unplug before something worse happened. Before I plugged the brush in, I noticed the brush would not stop vibrating no matter how long it had been even though it’s supposed to after a couple minutes. It did not stop until I plugged it in. This has happened one other time before a few months ago but it never got hot while charging before now. I will not be purchasing this brush again.",
                title="Fire hazard"
            ),
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/5179YiOxL8L._SL1500.jpg"),
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5.0,
            review="I've had the much more expensive Sonicare toothbrush for years and been happy with it, but it was always bulky to travel with and it finally was time to replace it.  Saw this and thought I'd give it a try.  LOVE the compactness of it - much more like holding a regular toothbrush - and honestly I don't need all of those different vibration/speeds - on my old toothbrush I just set it at one speed and kept it there - so the simplicity suits me well. I've traveled with it three times already and it travels perfectly.  Another reviewer had complained about it turning on during travel - if you use the brush cover as instructed it would never turn on - again, nice simple cover design. The battery has lasted over a month on a full charge.  Would buy it again!",
            title="Travels great and works well!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=4.0,
            review="I travel international, and It can be hard to find a toothbrush that's compatible with dual voltages, and then of course there's one more charger to carry with you. I love the fact this charges from a USB cable, and you can just plug it into your computer.\n\nWithout the case it's the size of a normal toothbrush. In fact, the travel case is probably a weak point. I don't even bother with it. I figure I'm rinsing the toothbrush head underwater before I use it anyway, so not overly concerned about germs or dirt. And how many of us put our standard toothbrushes in protective cases anyway? What I think would be better is just some kind of a cover for the actual bristles. Some of the other sonicare's have this.\n\nI've only tried this a few times, but to me it works just as well as my larger sonicare, although I agree it doesn't vibrate quite as fast after you use it once. To that end I would say charge it after each use. The battery is a fraction of the size of the larger sonicare.\n\nI ordered a couple extra heads, which I believe were $10 for two-- a fraction of the full-size sonicare. Overall I'm really pleased for the intended purpose, i.e. for travel. For daily long-term use I'm not trading in my full-size sonicare.\n\nUpdate: I used this for just shy of 90 days in Thailand, and it performed flawlessly. I think I charged it four times in that entire time. One other nice thing about this brush is unlike the Pro model I have at home with the stand that plugs into the wall, there's no buildup on this. The so-called pro-modern makes a big mess of my sink counter, and in general there's a big build up of tooth paste that leaks through the head. And since you're never completely getting your toothbrush dry, combined with hard water there's a huge amount of calcium buildup. That just doesn't happen with this brush.\n\nI would say there's a slight difference in speed from the Pro model, but I can't really say there's a significant difference in how clean my teeth are, as I tend to use this like a regular toothbrush and don't just hold it against my teeth. Overall I really like it. I'm ordering a 2nd one.",
            title="Great travel toothbrush"
        ),

        Review(
            buyer=sarah,
            product=product,
            rating=5.0,
            review="I was a Quip user for a while. I liked the look and I really enjoy the timing feature. I switched because the quip heads kept falling off mid brush, and brushhead replacements were getting too pricy. I found this Philips and it’s great! Love the color, the reasonably priced brush heads, the timer and the case for travel. I only wish it came with a holder for my mirror, but I’ll survive. Enjoying it!",
            title="Perfect"
        ),
    ])

    # https://www.amazon.com/Tracfone-Motorola-moto-Pure-32GB/dp/B09NWDJQ78/ref=sr_1_3?keywords=phone&qid=1673129825&sr=8-3&ufe=app_do%3Aamzn1.fos.18ed3cb5-28d5-4975-8bc7-93deae8f9840&th=1

    product = Product(
        seller=seller,
        title="Tracfone Motorola moto g Pure (2021), 32GB, Blue - Prepaid Smartphone (Locked)",
        price="519.99",
        description="Make sure this fits by entering your model number.\nDUAL CAMERA SYSTEM: Get professional-looking portraits with a blur effect using the depth sensor. The 13MP camera with phase detection autofocus (PDAF) captures your subject in the blink of an eye..Form_factor : Slate\nMORE FUN. LESS LAG: Feel your phone respond instantly to every touch, tap, and swipe using an octa-core processor with HyperEngine.\nWATER-REPELLENT. WORRY PROOF: Whether you’re going out for a run or getting caught in a little rain, a water-repellent design2 keeps your phone protected inside and out.\nBEAUTIFULLY DESIGNED. THROUGH AND THROUGH: Securely unlock your phone with just the touch of your finger.\nCARRIER: This phone is locked to Tracfone, which means this device can only be used on the Tracfone wireless network."
    )

    db.session.add_all([

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71zGrrAe5NL._AC_SL1500_.jpg"),
            preview=True,
            position=1
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71wQImiv9OL._AC_SL1500_.jpg"),
            preview=False,
            position=2
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71pLWLYN-rL._AC_SL1500_.jpg"),
            preview=False,
            position=3
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71IpaMmzQ5L._AC_SL1500_.jpg"),
            preview=False,
            position=4
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/81gp2lbffJL._AC_SL1500_.jpg"),
            preview=False,
            position=5
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5.0,
            review="Amazing phone for the money\nLenovo has done a fantastic job since it acquired Motorola.\n\nLike my prior Motorola fones, this one has minimal bloatware for a near stock Android experience.\nJust a few easy to remove pre-installed games, and easy to remove Facebook app as well.\nFM radio app can't be removed, but it was easy to deactivate.\n\nNote:\nThis fone will not work with a T-Mobile SIM, it requires a TracFone SIM.\nEven though TracFone does use in fact use T-Mobile towers, amongst others.\n\nDoes work perfectly with my Walmart Family Mobile SIM card (running T-Mobile), as WFM is 100% owned by TracFone.\nTherefore, my WFM SIM is actually a Tracfone SIM card, connecting to the T-Mobile network.\n\nNo tweaks during set up were needed, such as modifying the Access Point Name (APN).\nPut my SIM in, powered up, and followed prompts during set up.\n\nEven better, wirelessly copied all settings and apps from my old fone.\nFollowed prompts on both fones, to both grant and accept permission to copy.\nWith 55 apps, took about 1 hour, but a very easy and automated process.\n\nOnly \"downside\" of fone is large size, which is a plus for many.\nBut, I'm quickly getting used to moving from a 5.5 inch phone, to this 6.5 inch.\n\nAlso, greatly appreciate moving from a 16GB phone to this 32GB.\nBeing able to keep as many Apps as one likes, and without needing to clear cache weekly to free up space for existing apps, is a huge upgrade, and big convivence.\n\nYes, Apps can stored on an SD, but it's already near full of music, movies, and photos.\n\nI'm not a \"gamer\" so the 3GB of RAM works perfectly.\nNo lags even when multi-tasking, etc.\n\nMy only multi-tasking is listening to music via streaming or via an app from SD stored music, while a fitness tracker in running.\nWorked fine with prior Moto e6 2GB RAM fone, and still no problem with this 3GB RAM fone.",
            title="Excellent Value. Works w Walmart Family Mobile SIM as TracFone bought WFM in 2016 & Runs on T-Mobile"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=4.0,
            review="I dropped my LG Rebel Lte &amp; broke it. I first bought the ACL 3 to replace it. The ACL 3 was terrible, and even worse was I bought it from the Tracfone website and it would have cost more to return it than what I paid for it. Next I tried Blu View 2, which was on par with the ACL 3, that is to say, terrible, if not more so. Horrible camera, unresponsive buttons, etc. At least I bought it where I could return it right away. Next I picked this phone, the Moto G PURE on Amazon, and it's a keeper. Great pics with the 13MP camera, responsive buttons, easy layout, and easy to learn and use. The only thing I don't like about this phone,  which is not specific to this phone, is that it's a larger size than what my old phone was. It's only about 1.25\" longer, and .5\"  wider, but I have small hands, I do tend to drop things. I know all phones are bigger these days, but I hope they go back to giving the choice of smaller phones.",
            title="More Than I Expected"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5.0,
            review="This phone is solid, nice feel, good weight, attractive in looks and easy to use.  For it's price, it is a great phone. Even though my previous phone still works great, it is 16 GB and I was running out of memory for apps.  I had to start removing apps as with each update of each app, they seemed to bloat taking up more and more memory.  That led me to needing a new phone with 32 GB of memory which led me to this phone.  Previously I always used LG Tracfones but I read LG is no longer making inexpensive Tracfones which is probably why they are no longer on Tracfone's website.  I always wondered how the Motorola phones were so when I saw this at a great price I bought it.  I have not connected it to Tracfone service yet as I want to have it setup to my liking before I do.  Even though it is still Android there are some differences with the Moto settings and its use of the features that make me prefer the LG phones but nothing that would make me not like it or want to use it.  My only complaint is no where on the Amazon listing for this phone did it say whether it is GSM or CDMA so I don't know whether Tracfone in my area will accept this phone.  The packing list said CDMA but according to Motorola's website it is GSM.  Then I read that Tracfone was bought by Verizon and as of November 2023 Tracfone plans will be changed.  There is some confusion whether Verizon is still CDMA or not.  So I don't know whether I will be able to use this phone after Verizon takes over.  Or whether I would stay with Verizon depending on their pricing policies for previous Tracfone customers.  But it is still a great phone so far.",
            title="Solid phone with great screen"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=4.0,
            review="Nice phone.  Migrating from a Samsung J3.  As others stated, this is an inexpensive phone.  Don't compare it to a $1k iPhone.  I thought it was a very good value for the price.\n\nThe negative comes from the service, Tracfone.  The lesson I learned is that you should just go to your local Walmart/Best Buy/etc. and buy a Tracfone phone from there.\n\nThere is an issue, and you will read about it in other reviews, where this phone (and I suspect other phones sold by Amazon) does not work with the Tracfone network where I live.\n\nI spent approximately 8 hours of the course of 2 or so weeks on support calls with Tracfone.  They could not figure out why the phone would not work.  Everything on their end was set up correctly.  But my phone did not have service.\n\nIn the end, I returned this phone and went to my local Walmart and bought a similarly priced phone, activated it and had no issues using Tracfone service.",
            title="Good phone, poor support from Tracfone"
        ),

        Review(
            buyer=sarah,
            product=product,
            rating=4.0,
            review="Purchased for someone who would really rather have a flip phone &amp; isn't fond of technology.  Works with TracFone as promised. Set up was a chore because it needed a Google account to transfer contacts from old phone.  Loaded with unnecessary apps (games mostly) which we deleted.",
            title="Easy to use"
        ),
    ])

    # https://www.amazon.com/TracFone-View-Prepaid-Smartphone-Locked/dp/B09XFJY4N4/ref=sr_1_4?keywords=phone&qid=1673129825&sr=8-4

    product = Product(
        seller=seller,
        title="TracFone BLU View 2 (2022) 4G LTE, 32GB, Sim Card Included, Black - Prepaid Smartphone (Locked)",
        price="29.22",
        description="The all new BLU View 2 smartphone pushes the limit to the edge with a gorgeous 5.5” HD+ Incell display, 64-Bit Quad-Core processor, 13MP Main Camera with Flash, and 8MP Camera for selfie lovers!.Form_factor : Smartphone\n5.5\" HD+ Incell Display; Android 11; Quad-Core 2.0GHz Processor; 3,000mAh battery\n32GB Internal Memory (expandable to 128GB); 3GB RAM; 13MP Rear Camera; 8MP Front Camera; 4G LTE\nCarrier: This phone is locked to Tracfone, which means this device can only be used on the Tracfone wireless network.\nUnlimited Talk, Text and Data plans starting as low as $20/month"
    )

    db.session.add_all([

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61qTWOAsIPL._AC_SL1500_.jpg"),
            preview=True,
            position=1
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71wQImiv9OL._AC_SL1500_.jpg"),
            preview=False,
            position=2
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71pLWLYN-rL._AC_SL1500_.jpg"),
            preview=False,
            position=3
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/715GxH3+S1L._AC_SL1500_.jpg"),
            preview=False,
            position=4
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/716F7il+B1L._AC_SL1500_.jpg"),
            preview=False,
            position=5
        ),

        ReviewImage(
            review=Review(
                buyer=brian,
                product=product,
                rating=5.0,
                review="Edit 12/11/22: Adding a star. Today I put on the case I got for this phone. I noticed it had a small cut-out at the same location where I thought there was a chip in the phone's screen. Upon close inspection of the \"chip,\" it's actually a small machined cut-out from the glass. No idea why it's there, maybe to insert a tool to pop the screen off? Whatever the reason, it's not a defect. So unless I find something else that's a problem, this phone is major bang for the buck.\n\nI received this phone yesterday, so haven't used it much yet, but it seems fine functionally. Much better than the ZTE Majesty Pro Plus it is replacing. However, right out of the box [INCORRECT] it has a small chip in the bottom edge of the screen. [INCORRECT] You can see it in the photo, about 1/3 of the way from the left, in the middle of the mini-blinds reflection. I'm hoping that a screen protector will stop it from turning into a crack, because I'm keeping it. I had already called Tracfone and had them transfer my existing account onto it. Don't want to do it again, even though it was easy. Tracfone has come a long way in the ten years I've been with them.",
                title="Very good value so far"
            ),
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71u9yqwQPTL._SL1500.jpg"),
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=4.0,
            review="I needed to replace an older phone so chose this one. I've learned how to deal with the problems but it drops calls, won't hold settings, lost some of my contacts &amp; the camera is not nearly as good as my old phone. I wouldn't purchase this particular brand again.",
            title="Phone won't hold settings & camera not great"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=4.0,
            review="Bought three of these and great starter phone for young children. Only complaint would be volume disappears if used a lot.",
            title="Good cheap phone"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=4.0,
            review="Great phone for the price",
            title="Awesome"
        ),

        Review(
            buyer=sarah,
            product=product,
            rating=4.0,
            review="This phone works, the plan options from tracfone are affordable. You can do everything you need to from this phone. But it can be slow sometimes. Then again you get what you paid for.",
            title="If you need a smartphone and performance isn't a consideration then this is a good choice."
        ),
    ])

    # https://www.amazon.com/Power-battery-Unlocked-Motorola-Camera/dp/B08NWBY8YJ/ref=sr_1_5?keywords=phone&qid=1673129825&sr=8-5&ufe=app_do%3Aamzn1.fos.18ed3cb5-28d5-4975-8bc7-93deae8f9840&th=1

    product = Product(
        seller=seller,
        title="Moto G Power | 2021 | 3-Day battery | Unlocked | Made for US by Motorola | 4/64GB | 48MP Camera | Gray",
        price="249.99",
        description="Make sure this fits by entering your model number.\nUnlocked for the freedom to choose your carrier. Compatible with AT&T, Sprint, T-Mobile, and Verizon networks. Sim card not included. Customers may need to contact Sprint for activation on Sprint’s network. To use this Device on Verizon, first, provision your SIM through Verizon Wireless. Log in to your account on Verizon Wireless. Devices - activate or switch devices - activate.Optical sensor resolution:48 megapixels.Maximum display resolution:HD+ (1600x720) | 267ppi .Display Type:IPS.Form_factor : Bar\nUp to three-day battery. Capture more of life without stopping to recharge thanks to a 5000 mAh battery.Aspect Ratio: 19:9\n48 MP triple camera system. Take stunning photos in any light, as well as beautifully blurred portraits and incredibly detailed closeups.\n6.6\" Max Vision HD, display. Watch games, movies, and video chats come to life on an ultra-wide screen.\nHas a 2020 Qualcomm Snapdragon 662 processor, updated from the 2019 Qualcomm Snapdragon 665 in the moto g power 2020.Lag-free performance. Get more done without slowing down thanks to a speedy Qualcomm Snapdragon 662 processor.\nWater-repellent design3. Keep your phone safe from accidental spills and splashes.\nMy UX Your phone. Your experience. With My UX, your phone works the way you want. Control it with simple gestures, customize your entertainment settings, and create a look that’s one in a million. The new My UX. It’s all you."
    )

    db.session.add_all([

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61jKxwxAZFL._AC_SL1500_.jpg"),
            preview=True,
            position=1
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61wIgUmC8gL._AC_SL1500_.jpg"),
            preview=False,
            position=2
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71Mf9KkT7QL._AC_SL1500_.jpg"),
            preview=False,
            position=3
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71MiNDiFz1L._AC_SL1500_.jpg"),
            preview=False,
            position=4
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61e4CYbLwTL._AC_SL1500_.jpg"),
            preview=False,
            position=5
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/51-O870ze1L._AC_SL1500_.jpg"),
            preview=False,
            position=6
        ),

        Review(
            buyer=brian,
            product=product,
            rating=3.0,
            review="UPDATE: 8/26/2022 at the end. Not great.\n\nBought this for my Dad who needed to upgrade from his old Galaxy S7 Edge (also a security risk as it's no longer updated...yikes) and this was the most affordable option for him at that point in time that wasn't refurbished, used, or overpriced for what you're getting. (Man, there are a LOT of those.)\n\nPros:\n-Battery life. (When you hear \"all day battery\" they ain't kiddin'. Motorolla (really Lenovo) gives you a big, beefy battery with this thing.)\n\n-USB-C. (Yay! No more having to futz around with Micro-USB.)\n\n-Fingerprint reader and face unlock.\n\n-Android 11! (I really don't like 12 and have missed 11.)\n\n-They actually give you a charger! (Take *that*, Apple!)\n\nCons:\n-Performance isn't where it needs to be. (4GB of RAM sounds reasonable for Android, but it's kinda pushing it. The older 600 series Snapdragon is long in the tooth and showing its age, so it's not exactly a speed demon, itself.)\n\n-64GB of storage isn't exactly going to win any awards. (And much like any storage device with an operating system, the fuller it gets, the slower it runs. Use the Micro SD slot, people!)\n\n-Only 10w charging. (So no matter what brick you throw at it, it'll TurboCharge (their branding) but it won't be like a Google Pixel series phone, which is lightning fast by comparison.)\n\n-720p display. (Don't take that 1600 to heart, because you're not getting that. I'm not sure why they chose this display or this particular size, but it's a rough 720p as in it's barely there, but there nonetheless.)\n\n-Camera notch IN the display. (Not a cut-out, not at the top of the bezel, no. Smack-dab right in the screen (much like the Pixel 4/4a, onward.)\n\n-Screen is polarized. (If you wear certain sunglasses, you can't rotate this to landscape mode as you won't be able to see the screen. It's LCD and probably akin to a Nintendo Gameboy Color, but much better quality.)\n\nOverall thoughts:\nI can see why people had problems getting their Verizon service to work with this phone. I got it to work with a simple SIM swap but the texting was a pain as their texting services are now secured and this didn't secure them right out of the box. (I forget the setting, but it's in the Hamburger Bar settings menu, it's per user and not overall. It's a pain to work with, but it does work.) Phone calls and everything else (including E-911) work well, after finagling. So does Wifi calling. It's just a needless pain to set up, really.\n\nThe performance is okay, good even, if you let the AI in the phone follow what you do. (Sounds like a security risk, but it's actually a caching mechanism allowing the phone to know what you use the most and giving it priority over everything else.) Kinda like how you can use Optane memory in an Intel-based computer to speed up a HDD akin to using a Hybrid drive. (In its current form/update, the phone reminds me of a Pixel 2 in overall power.)\n\nThe screen could be better. You can see the individual pixels and the lines/rows they're in and they're so noticeable that you can actually be taken out of the moment with what you're watching/seeing when it happens. It is capable of displaying 1440p and 4k signals, still at 720p, but usually devices with smaller resolution screens get stuck at 480p or 720p signals and make the best of it while this can successfully take in those signals and at least cleans up the picture and makes it look like proper HD, even though it's at the low end of it. Buffering isn't nearly as bad because it's driving a 720p display, so movies and shows will load slightly faster because of it. (Within in reason. Some apps drag like they're being operated by snails until the stream fully loads. Ugh.)\n\nThe lack of stereo speakers is a real pain. (I miss my Pixel for that alone.)\n\nI traded my Dad my phone (Pixel 4a) for his (this one) because I can use it better (this is a MASSIVE phone) and the Pixel works better for him. This is capable enough for most people and it's quite usable. The hotspot feature works (you have to have a subscription with your carrier to use it), it works with Android Auto (very sluggish start up time...bleh), and for A/V stuff, it works well enough.\n\nFor the price? Solid phone. Especially when you consider it's brand new and not used or refurbished. That said, if you're fine with used/refurbished and want something with more power in the same price range, I recommend a Pixel 4a or 5/5a. Both will still be supported with updates through 2023 (possibly 2024) and have a solid feature set, whereas this will be using Android 11 for the foreseeable future (but with security updates!) and if you want Android 13 and beyond, you'll need a better/newer phone.\n\nI'm honestly more or less happy with it, the price was good for what you're getting (brand new), and it's a sturdy beast with a massive battery (by comparison). Recommended.\n\nUPDATE: Changing my final thought to mildly recommended. The phone still works, but the AI garbage is nothing but a sales pitch. The phone somehow seems to go slower, with some new feature or task you give it. The AI is supposed to be helping it learn which apps you use the most and adjusts itself accordingly. Well, the AI decided \"I'm going to use the slowest lane possible. We'll get there in 2 hours, instead of 30 minutes. Enjoy the ride!\" and boy, oh boy, does it crawl.\n\nIt's gotten to the point where using Android Auto is just almost completely impossible. Button presses/taps can take upwards of 30-60 seconds to register! (That's insane when you're supposed to be using it as a GPS!) YouTube music lost most of my songs and refused to play them, asking me to redownload them (and it never did), so there would be entire skip spots during any journey. (I had to pull over once to figure out what the heck was going on.)\n\nVoice commands are sluggish, reaction times are the equivalent of a newbie going up against Tyson in his prime. You take the swing, but nothing happens until after you needed it many seconds ago.\n\nEven outside of Android Auto, it's sluggish. Loading Chrome can be a nightmare, given the page you're checking out. *sigh*\n\nPart of the problem is the storage. Much like on a computer, eMMC (which is what a phone uses) can slow down once it's too full, and all storage drives (regardless of the type) all have a recommendation of keeping things at, or below, 50% of the storage. Well, that's impossible on this phone because nothing will install to the SD card and the Motorola bloatware takes up a good chunk of your available space. You can max out the storage on this thing in no time flat.\n\nIt's a great starter phone, it's fine if you're needing one in a pinch and can't afford more (believe me, I get it, I've been there more times than I can count.), but it's not going to be your #1 daily driver in the long run. Not unless you're fine with Motorola apps, chrome, some texting, and maybe some YouTube. Forget Android Auto, forget gaming, and forget packing a bunch of apps on here. It's clearly just a phone in a pretty Android wrapper.",
            title="A Beast Of A Battery, Not Such A Beast Of Performance"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=3.0,
            review="I will start with the 2 worst, most functionally-deficient things. I ended up returning it because of the first defect. Maybe they will patch it?\n\n1. The status bar is all messed up. This phone has the camera cutout as a little dot on the left, so that space can't be used. But it ALSO prohibits icons in a center area as if it had a medium-sized notch there, which it doesn't. This leaves space in the status area for no more than FOUR notification icons before it does a little dot thing as if you are overflowing. Did they forget to change the software from a previous model which had a giant notch there? It makes this phone unusable for me. I need a status bar with room for a bunch of stuff I have going on constantly. I need to see download and message statuses for multiple things. My current phone, a Blu XL4, has an option to ignore the top sliver of the display with the garbage \"notch\" so I have a full-width status bar. Motorola does not, AND they messed up the default. There is no way to use this phone if you need more than 4 icons visible.\n\n2. There is no screenshot icon in the pull-down menu. I need to take a lot of screenshots, and the power/volume combo is both annoying to use and wears out the buttons. Motorola's new method requires you to tap-and-hold with 3 fingers on the screen. The problem with that is it activates buttons/links/etc on a lot of pages. So you will need to download some shady 3rd-party app with adds or whatever if you want to add a screenshot function. It also has a (not)\"helpful\" menu which pops up every time you do a screen shot, which gets in the way.\n\n3. I don't use split-screen much, but if you do... you can't long-press the recent app icons to do this. Motorola's idea is to swipe from the center of the left edge of the screen (oh how clever, cut the screen in half!). Problem: THAT GESTURE IS ALREADY USED BY ALMOST EVERY APP to access menus. Did the genius who removed the long-press method to replace it with side-swipe not know this?\n\nNow some less-important details...\n\nOne good thing: it does have double-tap to wake the display. This should be standard. It saves wear on the power button and is sometimes more convenient depending on how you are using the phone.\n\nYou can't turn off a mystery feature which wakes the display in response to the slightest wiggle or movement.\n\nYou can't turn of a wallpaper animation which stretches your wallpaper and displays it in a distorted form, and then shrinks it to normal temporarily when you touch menus. Your wallpaper will spend most of its time blurred.\n\nThe fingerprint sensor can't lock the display. You must click the button. I don't know why. I had 2 other Motorola phones which would let you lock them by touching the sensor. Another way Motorola really wants you to click the power button constantly. The reason I prefer not to have the power button used for everything is because the only phone I had break in the past several years was a Moto E4, and the power button stopped working.\n\nAbout that camera... it's pretty good, but FYI it doesn't give you 48MP pictures (you kind of knew it wouldn't). They use a 48MP sensor and you end up with 12MP pictures. The idea is to reduce noise by averaging groups of 4 pixels. It works somewhat, and I like the pictures, but calling it a 48mp camera makes it sound much better than it is.",
            title="Very poor software makes it useless"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=4.0,
            review="I initially bought this phone for a friend that said her phone died.  Then she said she didn't want it and ordered herself an S22.  So I figured I'd keep the phone for myself, and I'm glad I did.\n\nMy everyday mobile phone is the Samsung Galaxy S22 Ultra.  But the swines that designed the thing, followed Apple over the cliff and took out the 3.5 mm Headphone Jack, did away with removable storage, and put the fingerprint reader in the middle of the screen.  This phone, being a budget phone, choose to not jump on the bandwagon of taking away features and charging you more money.\n\nI use this phone as my primary media player.  It takes good enough pictures and videos, everything works as expected.  I put a 128 GB SD card with all my favorite movies.  And with Bluetooth and the 3.5mm jack, I get the best of both worlds.  I can receive calls with the Google Voice app, but again, corporate swings, took away the ability to make WIFI calls using the google voice app.\n\nIt has the same size battery as the S22 Ultra, so on standby, it can go for up to a week without needing to charge.  And since there's WIFI just about everywhere these days, I use this phone about as much as my S22.\n\nI could go on and on about why you should buy this phone, but you should be aware of two points.  Its a budget phone, so speed is not its thing.  Also, some popular apps, for some reason, doesn't work on it.  The most notable is the Facebook Messaging app.  It loads but is unresponsive.  That aside, great budget phone.  Strong buy recommendation.\n\nUpdate.  All i had to do was update the Facebook messenger app and it started working again.",
            title="Outstanding value for the cost. Highly recommend."
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5.0,
            review="Superó nuestras expectativas y no tuvimos ningún problema para activar el chip de nuestra operadora, ni para activar las aplicaciones que necesitamos.\nExcelente relación calidad &gt; precio.\nMuy buen dispositivo. A mi esposita le encantó.",
            title="Excelente dispositivo."
        ),

        Review(
            buyer=sarah,
            product=product,
            rating=1.0,
            review="",
            title=""
        ),
    ])

    # https://www.amazon.com/Apple-iPhone-XR-Fully-Unlocked/dp/B07P6Y8L3F/ref=sxin_17_cpf_saw-CPFPecos-dsk-lmlk-asin?content-id=amzn1.sym.0f1b45b9-2ef3-449d-8dec-0cc7749915dc%3Aamzn1.sym.0f1b45b9-2ef3-449d-8dec-0cc7749915dc&cv_ct_cx=phone&keywords=phone&pd_rd_i=B07P6Y8L3F&pd_rd_r=e54d7e73-5d2f-4af0-abc8-02eea24545f8&pd_rd_w=ykA6q&pd_rd_wg=HdXXO&pf_rd_p=0f1b45b9-2ef3-449d-8dec-0cc7749915dc&pf_rd_r=SEQHS4NM9SJASW70G8DV&qid=1673129825&sr=1-1-88bb4e7b-fb79-43dc-9dec-6da196f88672&th=1

    product = Product(
        seller=seller,
        title="Apple iPhone XR, US Version, 64GB, Red - Unlocked (Renewed)",
        price="215.55",
        description="This phone is unlocked and compatible with any carrier of choice on GSM and CDMA networks (e.g. AT&T, T-Mobile, Sprint, Verizon, US Cellular, Cricket, Metro, Tracfone, Mint Mobile, etc.).\nTested for battery health and guaranteed to have a minimum battery capacity of 80%.\nSuccessfully passed a full diagnostic test which ensures like-new functionality and removal of any prior-user personal information.\nThe device does not come with headphones or a SIM card. It does include a generic (Mfi certified) charger and charging cable.\nInspected and guaranteed to have minimal cosmetic damage, which is not noticeable when the device is held at arm's length."
    )

    db.session.add_all([

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/51QG+K5RQtL._AC_SL1500_.jpg"),
            preview=True,
            position=1
        ),

        Review(
            buyer=brian,
            product=product,
            rating=4.0,
            review="The phone I received was by all estimations brand new. Not a mark on it and fully charged. However, being new to the Apple World, I can honestly say Windows &amp; Android are both in plain, simple, super easy to understand English. Apple is not. Even its keyboard is not a full Standard Keyboard, like it is with Windows &amp; any Google machine. Android is Google, that's why I say it that way. No getting around it. Just keeping it short &amp; to the point. Apple's iPhone keyboard takes extreme amount of effort to use because it is not the Standard keyboard of every other operating system. Thankfully, I was able to connect a Bluetooth keyboard to it. Otherwise, it's a serious no-go for keyboard use.\n\nAs for Apple's iPhone Touchscreen, again, I find it sorely lacking. There's no such thing as the simple pinch &amp; zoom on it. That particular luxury seems to be found only within the Camera &amp; Picture sections. You'd think it'd at least be within the iBook section but it's not. On most everything Windows or Google, every app is not just touch &amp; activate, but also affords the luxury of pinch &amp; zoom as well as easy swipe &amp; easy app close &amp; dismiss. Can't say that about the Apple iPhone.\n\nAnd for some unknown reason its WiFi also keeps turning itself on. I can't seem to keep it off no matter how often I manually turn it off.\n\nFor Apple being so USER-FRIENDLY, I cannot at all say that it is. In fact, IT IS ANYTHING BUT USER-FRIENDLY.  If the Apple World was so user-friendly, then it would be a very simple and easy transition from the Windows or Google platform to Apple. And I can honestly say it is Not at all simple or easy. I was so hoping it would be as simple &amp; easy as my Windows machine &amp; Android phone, but sadly, it's actually quite maddening.\n\nIf you enjoy Kindle reads, you'll need to install the app for it. But I can also tell you, Apple's iBook seriously pales in comparison to Kindle. Ironically, the Google Search Engine is installed on Apple's iPhone but Kindle is not. I avoid Google anything &amp; everything as much as can be done. But for Apple to deny Amazon's Kindle Apple on its phones, seems almost a crime.\n\nI have yet to install the Kindle reading app or to test out the camera on the iPhone. When I do I'll update my review. But currently I can't say it's anything to brag about. And I most certainly did not expect to see Google's Search Engine/Web Browser on it.\n\nSize wise, it's the exact same size as my Sony Xperia Z3v. It still functions quite well. Not perfect, but well enough for me since I have it locked to call, text, Kindle reads &amp; camera.  I can easily read, pinch &amp; zoom &amp; highlight my Kindle reads, pictures &amp; text messages on it. Can only do that with pictures on the iPhone. So for it being so great, I actually find it quite limiting. Not because it's an iPhone, but because the Apple creators decided to create a platform that is quite complex and extremely arduous to use. Apple created its own \"language\" that must be learned in order to navigate the complexities of its Eco-system.  Even now, trying to login to the Apple App Store, no keyboard appears so I can actually install Apps necessary for my personal use. Yet you're required to sign in to it. How can you sign into the App Store when NO KEYBOARD APPEARS TO LET YOU?! So, even if I did not want to use the phone feature, but instead use it as a computer tablet, I cannot because it won't let me login to the App Store. ... Like I said, to anyone new to the Apple world, it's quite a infuriatingly maddening conundrum. If Apple wants to gain new customers and retain them, then Apple needs to change how it operates. And if Apple is supposed to be the safest of all online platforms, then it should not sport Google's web browser.\n\nThe phone I received was/is like brand new. Operating it though, takes considerable patients as it is quite the learning curve. It should not be so difficult to transition from Windows, Android or Google to Apple. They all made sense to everybody from the moment they came out because they were in simple English and easily understood and simple to navigate because of it. Apple on the other hand, not by a long shot. Even Apple's touchscreen capabilities sorely lacks in comparison. And that's sad. You'd think their touchscreen capabilities would be at least on-par with Windows, Google &amp; Android but it is not. You'd think Apple's touchscreen capabilities might even be better than Windows, Android &amp; Google, but no. Thus far I can find nothing to brag about regarding Apple anything. I was so hoping to find something better about Apple. Instead, I'm greatly disappointed and left seriously frustrated.\n\nThe iPhone itself came fully charged and appears in brand new condition. It also came with an original Apple Charger.\n\nI give the seller a stellar 5 star rating, along with the iPhone I received.\n\nI give Apple itself a mediocre 3, even 2 star rating.\n\nSo to anyone new to the Apple world, maybe an iPad would be easier to use. I started with a phone since I need both a new phone &amp; a new computer and figured Apple would be a serious upgrade to Windows and for sure compared to Google's Android. ... Apple is not at all user-friendly to a first time user. Only Windows, Google &amp; Android can actually claim user-friendly bragging rights, from day one for any first time user.\n\nApparently I need either direct Apple support or YouTube's Apple education in order to learn how to make the best use of this phone.  I don't fault the phone for anything. It's an Apple thing. It's very nearly like you gotta go to MIT to learn it. And that's just not right.\n\nWill update as I learn how to navigate Apple's world &amp; extremely clunky Eco-system.\n\n1st Time Apple iPhone User Assessment. -\nPhone - good. - can't give it high marks due to Apple itself.\nApple - not worth all the money &amp; certainly nothing to brag about.",
            title="1st Time Apple iPhone User"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=4.0,
            review="I ordered 2 of these one black and one in red. Both phones came the same day same package. They were in great shape. Some noticeable cosmetic damage. Not much. For 100$ cheaper than retail price of being brand new you really get the bang for your buck here. The phones were shipped on the 13th the day of ordering and received them on the 15th of that same month “2 days later”. Like I said some minor damage not much. Definitely almost looks brand new. You will receive a lightning charger in the box. My Advice if you purchase is to also purchase a “type c to lightning charger” used on the new iPhones because it will charge when you are in a jiffy and I mean completely charged within a hour! The phones are unlocked to any carrier in the US I cannot speak for other countries. All in all I do recommend this product to anyone and I also would rate this on a scale from 1 to 10 it would be a 8.5 out of 10 and only because the minor scratches on the aluminum part of the phone but definitely not very noticeable! I am very pleased with this product as I just saved almost 300$ Because I didn’t have to purchase brand new and I still got 2 that look absolutely perfect and work amazingly!",
            title="Great phone"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5.0,
            review="While the phone is impressive upon opening the Apple box, and the features built into it are great, the phone battery is not.  Heats up after 20 minutes and I mean HOT!  I bought three phones for gifts this Christmas and decided on refurbished because I had to buy three.  Out of the box they are flawless and upgrading them to 16.0 was easy enough but the batteries all heat up just a few minutes into the upgrade.  That just isn't right.  I have bought straight from Apple store since the iPhones came out and never had a problem with overheating.  New battery replacement is pricey which makes this refurbished phone not as great a deal at all.  I just don't know how long they will last and I feel unsettled about that.",
            title="Works"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=4.0,
            review="I purchased this phone back in July 2021. I meant to write a review six months in- just to let others that are considering a purchase, how the phone is holding up. It’s 2023 and I’m still using it and have no issues with it as of today.\n\nThe reason it’s only four star instead of five is because for a moment, there was a small problem with the screen turning black and having the small loading circle appear (it would happen for ten to thirty minutes) but it hasn’t happened for months now, so I’m going to assume it won’t happen again.\n\nAll in all, the phone is still reliable and works wonderfully.",
            title="A year and some later"
        ),

        Review(
            buyer=sarah,
            product=product,
            rating=4.0,
            review="I purchased this phone with the intent of having it for a very short period of time.  My plan was to use it as a trade-in since my previous phone was too old to qualify (iPhone 6 Plus).  I purchased the phone for around $250 and got an $800 trade-in value on an iPhone 14 Pro Max, when switching from one carrier to another.  I'd been with the previous carrier for 20 some years but it was time for a change.\nThe only thing that kept me from giving this 5 stars, is that it had non-Apple parts on it that the new carrier was somehow able to identify, maybe battery, maybe screen?  Perhaps there is some history somewhere of previous iPhone repairs.  Anyway, the replacement parts were determined to be acceptable and the $800 credit was given.  I ended up using the phone for a couple of weeks while waiting for my new phone to come in.  The phone functioned to my satisfaction.\nI didn't rate the face recognition because after two attempts, I did not get it to work.  My wife said I wasn't doing it right and that may be the case.  I was trying to follow the camera with my eyes when moving the phone around in the circle.  The app completed, be then said I was unable to use face recognition.  The front camera did work, so again, perhaps the failure was unrelated to the phone.\nFor anyone who wants to try to save a few hundred dollars on trading in a phone, this may be the way to go.  As I found out though, there could potentially be some risk depending on the parts used for any repairs made.",
            title="Arrived on time, packaged well, and in very good condition."
        ),
    ])

    # https://www.amazon.com/Apple-iPhone-Fully-Unlocked-Refurbished/dp/B07756QYST/ref=sxin_17_cpf_saw-CPFPecos-dsk-lmlk-asin?content-id=amzn1.sym.0f1b45b9-2ef3-449d-8dec-0cc7749915dc%3Aamzn1.sym.0f1b45b9-2ef3-449d-8dec-0cc7749915dc&cv_ct_cx=phone&keywords=phone&pd_rd_i=B07756QYST&pd_rd_r=e54d7e73-5d2f-4af0-abc8-02eea24545f8&pd_rd_w=ykA6q&pd_rd_wg=HdXXO&pf_rd_p=0f1b45b9-2ef3-449d-8dec-0cc7749915dc&pf_rd_r=SEQHS4NM9SJASW70G8DV&qid=1673129825&sr=1-2-88bb4e7b-fb79-43dc-9dec-6da196f88672&th=1

    product = Product(
        seller=seller,
        title="Apple iPhone 8, US Version, 64GB, Silver - Unlocked (Renewed)",
        price="148.94",
        description="This phone is unlocked and compatible with any carrier of choice on GSM and CDMA networks (e.g. AT&T, T-Mobile, Sprint, Verizon, US Cellular, Cricket, Metro, Tracfone, Mint Mobile, etc.).\nPlease check with your carrier to verify compatibility.\nWhen you receive the phone, insert a SIM card from a compatible carrier. Then, turn it on, connect to Wi-Fi, and follow the on screen prompts to activate service.\nThe device does not come with headphones or a SIM card. It does include a generic (Mfi certified) charger and charging cable.\nTested for battery health and guaranteed to have a minimum battery capacity of 80%."
    )

    db.session.add_all([

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/51hy7WpydQL._AC_SL1500_.jpg"),
            preview=True,
            position=1
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/510vS06sASL._AC_SL1500_.jpg"),
            preview=False,
            position=2
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/51hy7WpydQL._AC_SL1500_.jpg"),
            preview=False,
            position=3
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/51Gt-Y1LA6L._AC_SL1500_.jpg"),
            preview=False,
            position=4
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/51yJUc7UJdL._AC_SL1500_.jpg"),
            preview=False,
            position=5
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/51hy7WpydQL._AC_SL1500_.jpg"),
            preview=False,
            position=6
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/510vS06sASL._AC_SL1500_.jpg"),
            preview=False,
            position=7
        ),

        ReviewImage(
            review=Review(
                buyer=brian,
                product=product,
                rating=4.0,
                review="When I bought the phone it seemed fine. But some of the color was scratched off near the charger port and around the lenses . I brushed it off because it wasn’t bad and I had a case to cover it. But the battery is where the problem is.When I ordered the phone it said in the description that the battery capacity would be at least 80% at the minimum and I bought the phone in excellent condition. But after being on the phone for 3 hours it was already at 45% (Dark mode, Low power mode, low brightness) when I went to check the battery capacity it was at 79%. I know it’s only a 1% difference but cmon. The battery life seriously is below average. Otherwise everything else is fine.\nUpdate: I talked to a customer service representative and she was very nice and helpful and helped me with the problem. Appreciate it.",
                title="undefined"
            ),
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61Z2fYqaozL._SL1500.jpg"),
        ),

        ReviewImage(
            review=Review(
                buyer=caitlynn,
                product=product,
                rating=4.0,
                review="What I didn’t like:\n1. How the bottom speakers were fully covered in dust. (NOTE: I forgot to take a photo since I immediately used an old toothbrush to clean it. Luckily, took a video. So here’s a screenshot.)\n2. The 82% battery life while others got 90+%.\n3. How the phone was packed in a flimsy plastic and only had 1 layer of bubble wrap.\n\nWhat I liked:\n1. How fully functional the phone was.\n2. The fast face recognition.\n3. It came with a pre-installed tempered glass.\n\nVerdict:\nDespite the awful packaging and the bottom speakers literally being filled with dust, at the end of the day, the phone performs well.",
                title="undefined"
            ),
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/413xhMTaBmL._SL1500.jpg"),
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5.0,
            review="I bought this iPhone 11 to replace my son’s SE. I usually buy refurbished for my kids because, well, they’re kids. They can buy new if they want when they grow up and get jobs. Anyway, we had no problem setting up the phone except for the cellular service. The box came with a tool for a SIM card which I thought must be standard but thought the old SE phone didn’t have a SIM. I was wrong. We took it to the Verizon store and the customer rep took less than a minute to change the SIM card to the new phone and we were all set. All data transferred seamlessly. So far, a great experience and everyone is happy.",
            title="undefined"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=4.0,
            review="Even though the 1st phone that was sent had an battery issue, which prevented me from setting up the phone, the seller was awesome with a quick response and solution. The seller overnight another one and tested it before sending it out. That one works perfectly. This was a Christmas present for my daughter and with just a few days before Christmas everything worked out, she absolutely loves this phone. Thank you to the seller for being a part of that joy brought to my daughter for Christmas.",
            title="undefined"
        ),

        Review(
            buyer=sarah,
            product=product,
            rating=4.0,
            review="Physically nice looking phone. However; battery was marked as 86% health on pkg but was actually 84% which is a bit less than I was hoping for. The BIGGEST issue is some sort of “white out” thing that randomly happens between screens. Several times while texting and adding a photo, the screen will white out causing me to have to reboot. Not sure if it’s software or hardware issue as I’ve never experienced such with prior iPhones. A little pricey but that was my choice.",
            title="undefined"
        ),
    ])

    # https://www.amazon.com/Samsung-Galaxy-128GB-Cloud-Mint/dp/B08L34NZDM/ref=sr_1_6?keywords=phone&qid=1673129825&sr=8-6&th=1

    product = Product(
        seller=seller,
        title="Samsung Galaxy S20 FE 5G, 128GB, Cloud Mint - Single SIM - Unlocked (Renewed)",
        price="226.00",
        description="This phone is unlocked and compatible with any carrier of choice on GSM and CDMA networks (e.g. AT&T, T-Mobile, Sprint, Verizon, US Cellular, Cricket, Metro, Tracfone, Mint Mobile, etc.).\nPlease check with your carrier to verify compatibility.\nWhen you receive the phone, insert a SIM card from a compatible carrier. Then, turn it on, connect to Wi-Fi, and follow the on screen prompts to activate service.\nThe device does not come with headphones or a SIM card. It does include a charger and charging cable that may be generic.\nTested for battery health and guaranteed to have a minimum battery capacity of 80%."
    )

    db.session.add_all([

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61cNFRPvMUL._AC_SL1500_.jpg"),
            preview=True,
            position=1
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61DFDYOPTeL._AC_SL1500_.jpg"),
            preview=False,
            position=2
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61szZqiFEOL._AC_SL1500_.jpg"),
            preview=False,
            position=3
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/41Vc4WIknzL._AC_SL1500_.jpg"),
            preview=False,
            position=4
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61uw2JhF5wL._AC_SL1500_.jpg"),
            preview=False,
            position=5
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/617bELa6dhL._AC_SL1500_.jpg"),
            preview=False,
            position=6
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61z+y4t+UhL._AC_SL1500_.jpg"),
            preview=False,
            position=7
        ),

        Review(
            buyer=brian,
            product=product,
            rating=4.0,
            review="12/29/22 update (read old below)\nWhy buy the latest phone if the previous model feels like brand new &amp; features are the same as new model. The s22 is about $700 to over $1k. While this 2yr old model is $220. I will use this minimum 4 years.\n\nMy old phone is almost 6 yrs old samsung s8 with 10k text &amp; many apps. So spent 1.5 hours at my phone carrier store. They transfered all my data to this phone.\nMy new used phone was originally Verizon &amp; after getting set up I notice my start screen shows VERIZON. I am not VERIZON! No big deal.\nLast night I spent a lot of time on lots of app sign up then the annoying UPDATES that feels like 100 updates. I think maybe 28 updates. Be patient.\nToday is my 2nd day playing with my new refurbished s20 fe. Ordered my case I think this phone is a keeper. Like new condition. No scratch.",
            title="undefined"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5.0,
            review="So, nice phone, great condition. HOWEVER Verizon is NOT supporting their older 3G system and only supports 5G and I could NOT send or receive  voice calls with the original sim card I had. A trip to Verizon store fixed this issue thanks to a tip from the vendor here. Nice guy, helped resolve what was an issue i would have had to do a return on. Always get an updated sim card if you are a verizon customer, even if the Sim is only a couple years old.",
            title="undefined"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=4.0,
            review="Sí fue lo que esperaba y estoy contento con ello, lo compré desde México y no hubo problema con el envio. Con algunos arañazos en el marco metálico y marcas del anterior dueño en la parte plástica para mí valió la pena por el costo y siendo la versión SD 865 5g difícil de encontrar en México por un mejor precio. Prende como TMobile y nunca desaparecerá su logo en el reinicio pero acepta cualquier SIM como Telcel 5g. Ya llevo un par de semanas con él y no ha tenido falla alguna, se calentaba un poco los primeros días y ahora solo cuando juego algo pesado. Si no eres en extremo exigente es una buena compra, no es la experiencia de abrir un dispositivo nuevo de fábrica pero ofrece mucho por el costo y la neta salió bien.",
            title="undefined"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=4.0,
            review="",
            title="undefined"
        ),

        Review(
            buyer=sarah,
            product=product,
            rating=4.0,
            review="Got the phone, transferred the Sim and SD card from s9+ turned on and worked without any problems. Used Samsung Smart Switch and Google play to transfer apps and files from old phone to the new phone. Had to re-setup all the MFAs I use for work, but was expecting that. Love the in screen fingerprint scanner. Much easier to use then the back scanner I used on the S9+. It will miss from time to time, but especially at work where I have to do MFA authorizations many times throughout the day when connecting to user's computers and servers to check settings or perform remote fixes it is so much easier to press my thumb to the front of the screen than having to pull off the wireless charger to scan from the back. Battery life is great. Old S9+ could barely make it through a normal 8 hour shift and sometimes it wouldn't. The S20 FE makes it through a 12 hour extended shift with more than normal MFA with 27% battery still left. Can't really speak to the camera as if I am wanting to take good pictures I will pull out the Canon Rebel. For quick snaps of serial numbers, model numbers and things like that it works fine. Hands free is much clearer than on the S9+ as I don't get crackling or distortions on the S20 FE. A good phone for a refurbished one.",
            title="undefined"
        ),
    ])

    # https://www.amazon.com/Samsung-Galaxy-128GB-Prism-Black/dp/B082T4F34B/ref=sr_1_9?keywords=phone&qid=1673129825&sr=8-9&th=1

    product = Product(
        seller=seller,
        title="Samsung Galaxy S10e, 128GB, Prism Black - Unlocked (Renewed)",
        price="139.99",
        description="Fully Unlocked: Fully unlocked and compatible with any carrier of choice (e.g. AT&T, T-Mobile, Sprint, Verizon, US-Cellular, Cricket, Metro, etc.), both domestically and internationally.\nThe device does not come with headphones or a SIM card. It does include a charger and charging cable that may be generic.\nInspected and guaranteed to have minimal cosmetic damage, which is not noticeable when the device is held at arm's length.\nSuccessfully passed a full diagnostic test which ensures like-new functionality and removal of any prior-user personal information.\nTested for battery health and guaranteed to have a minimum battery capacity of 80%."
    )

    db.session.add_all([

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71bK3oKRCOL._AC_SL1500_.jpg"),
            preview=True,
            position=1
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61I00YEn5yL._AC_SL1500_.jpg"),
            preview=False,
            position=2
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/41Ez2Yk5suL._AC_SL1500_.jpg"),
            preview=False,
            position=3
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/51LQFZBi+IL._AC_SL1500_.jpg"),
            preview=False,
            position=4
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/51lY9gdyQpL._AC_SL1500_.jpg"),
            preview=False,
            position=5
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/41ED8gTKItL._AC_SL1500_.jpg"),
            preview=False,
            position=6
        ),

        Review(
            buyer=brian,
            product=product,
            rating=4.0,
            review="First off, these are great phones IF you get a good one. I've ordered three of these because they are fantastic phones in a pocketable size. At $149 these are great for kids or anyone that doesn't need the latest and greatest but still wants a nice phone.\n\nTwo of the phones arrived in PERFECT condition, functioned flawlessly, had good batteries and matched the item description. The 3rd phone was returned because it had small bubbles under the screen, a dented charging port, and lots of scratches. Not only that, there was dirt or rust in basically all the ports. It wasn't even cleaned, let alone \"renewed\".\n\nMy advice is to read the SELLER reviews and don't buy from anyone with less than a 90% seller rating. Chubbiestech is fantastic. Their items are well packaged and generally in perfect condition. OlympicWireless was a mixed bag with one of the phones being perfect and another being unacceptable (see above). OlympicWireless also used oversized boxes with no padding or protective films...so your new phone just bounces around inside a box on its way to your door. Chubbiestech used appropriated sized boxes with official \"Amazon Renewed\" packaging and protective films. Obviously I highly recommend Chubbiestech if you can buy from them.\n\nBe aware that the seller of this phone changes frequently and the seller you buy from will make a huge difference in the device you receive. There are also frequent price changes and sometimes it will be Prime...and then 3 minutes later it won't be. Make sure you buy Prime for easy returns in case you are less than thrilled with the condition. Keep exchanging until you get a phone in near perfect condition from a good seller.\n\nThese are 5 star phones when you get one that's as described in the item listing. I took off one star just because it seems to be a roll of the dice on which seller will send you a good one.",
            title="undefined"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5.0,
            review="De envío a México llegó antes de lo esperado.\nEs un poco más pequeño de lo que esperaba pero te acostumbras.\nTengo entendido q hay varios tipos de calidad, así q enteré más bajo mires te llegará con defectos.\n\nSi eliges la condición excelente fácil es un teléfono nuevo, obtuve un 91% de vida en la batería.\nTengan en cuenta que al ser un teléfono potente el drenaje de la batería es medio alto aunque el tamaño de la pantalla lo compensa, así gasta menos. Recomiendo q quiten todo en segundo plano excepto aplicaciones q ocupen, para eso hay una opción en ajustes de batería. Al hacer eso el drenaje de batería se reduce considerablemente y más si usas ahorro de energía (Si utilizas ahorro de energía no notarás un cambio en la potencia).\n\nTodos se quejan de que carga lento con el cargador genérico, en ajustes de batería hay una opción que relantiza la carga desactivenla la opción es \"carga rápida\" hagan pruebas si no me creen, ese modo hace lenta la carga y les manda el aviso de precaución.\n\nEs buen teléfono mide casi una pulgada menos que una pantalla de 6,5\".\nEsta bien equilibrado el peso, aunque no noto una diferencia en que tenga cristal ._. creo solo es marketing (el cristal siempre está frío).\n\nLa cámara tiene un POV muy amplio así que si tienes manos grandes probablemente puedas tapar una parte de la imagen, no noto un cambio grande en la cámara, es normal pero en ciertos puntos sobresale de otras. Pero lo que si me gustó es la grabación de video.\n\nLos micrófonos y el audio del Celular me encantaron, por eso si valió la pena (el audio es el que más me gustó).\n\nLa pantalla no es una diferencia muy grande o algo que resalte demasiado simplemente es otra pantalla Amoled. Pero resbala bien al estar usando la pantalla.\n\nDe la batería ya hablé jajaj, quita las cosas en segundo plano y usa ahorro de energia. Con eso la duración es excelente, más de 7 u 8 hrs de uso normal o moderado, hasta podría decir q intenso.\nIgual, existe la opción de jugar conectado si tanto les molesta la duración ._.\n\nEsta es una opinión para aclarar dudas si es que creen q llegan muy usados, la respuesta es no, depende la condicion q eligan ustedes es mi primera vez usando Amazon renewed y creo para los demás es igual. Espero les sirva, y si, si es liberado jajajaj.",
            title="undefined"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=4.0,
            review="",
            title="undefined"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=4.0,
            review="Much better than my previous $70 Samsung Galaxy Core, lol.\nLoaded with software from Samsung. No use for it.\nAnd can't remove at all the Bigby application or disable the button. Keeps popping up the Bigby's app. Can reassign the button to something else but requires logging into a Samsung account, blah blah. Ridiculous.",
            title="undefined"
        ),

        Review(
            buyer=sarah,
            product=product,
            rating=1.0,
            review="I bought this phone to use on europe and so far everything is working perfectly, the phone is practically new, no scratches or anything (I might have been lucky). I was concerned that the battery would be horrible as some reviews on the internet say, however it is similar to my last phone so not a problem.",
            title="undefined"
        ),
    ])

    # https://www.amazon.com/Simple-Mobile-Samsung-Galaxy-Black/dp/B0BBXD7S5R/ref=sr_1_10?keywords=phone&qid=1673129825&sr=8-10#customerReviews

    product = Product(
        seller=seller,
        title="Simple Mobile Samsung Galaxy A03s, 32GB, Black - Prepaid Smartphone (Locked)",
        price="49.88",
        description="Capture life on the go in perfect detail with a 13MP main camera.\n6.5\" HD+ LCD display, and 32GB storage expandable all the way up to 1TB.\nRelive your memories all day long with a 5,000mAh battery.\nThis phone is locked for use with Simple Mobile.\nCompatible with Simple Mobile Unlimited talk, text & data plans starting at $25/mo."
    )

    db.session.add_all([

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/812woqv69CL._AC_SL1500_.jpg"),
            preview=True,
            position=1
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61ij9SFXg0L._AC_SL1500_.jpg"),
            preview=False,
            position=2
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/81123iMH9TL._AC_SL1500_.jpg"),
            preview=False,
            position=3
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61qLp9a-bAL._AC_SL1500_.jpg"),
            preview=False,
            position=4
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71B7LL75H6L._AC_SL1500_.jpg"),
            preview=False,
            position=5
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71n9hiFWJhL._AC_SL1500_.jpg"),
            preview=False,
            position=6
        ),

        ReviewImage(
            review=Review(
                buyer=brian,
                product=product,
                rating=4.0,
                review="&nbsp;This phone is one of the best cheap phones that costed under $40 for me, the battery life is astonishingly amazing for such a cheap price and same goes for the display as well. It even gives off that flagship feel and look even though it is a budget phone. Even the camera is surprisingly well with 3 on the back for a wide view and 32GB of storage to hold my video in. The casing on it can withstand 1 meter drops onto a hard surface without any damage to it on every side. Seemless navigation with with gestures and buttons and motion with transition effects are always smooth including the One UI Home launcher. A few additional apps offered during setup from both TracFone and Google Play Store per usual but keep in mind some random games and social apps like TikTok and SnapChat will randomly install itself after you connect it to Wi-Fi during the setup process even after the setup is complete which takes up a whole gigabyte of storage but you can uninstall these apps right afterward (Facebook is pre-installed into the system so you can only disable that). However keep in mind right afterward you finish the setup of the device, update it to android 12 before putting any data on it because it might get stuck and you'd have to factory reset it to do the setup all over again, after that everything is good just do the setup again and remove the apps that install themselves and you're good to go. Another downside is that some notable standard features such as sound customizations like amplifier and equalizer are missing from the settings as well as screen recorder/screenshot tools are also missing from the quick panel even though those are also supposed to come standard with all One UI devices. I can't seem to find Good Lock in the Galaxy Store and Sound Assistant doesn't work right without the sound equalizer feature. I understand it has no Bixby features since this is a budget device and not a regular mid range A series or flagship, but some of the essentials I like using on my other One UI devices aren't there or are supported. However in the end this device has amazing hardware for the cheap price and the functionality can really be amazing for what you'll get out of a budget phone. -Kai Edward Bannon, Android technology expert",
                title="undefined"
            ),
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/51RGUSqnb0L._SL1500.jpg"),
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=2.0,
            review="There was no wall charger to charge the phone",
            title="undefined"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=1.0,
            review="This didn’t come with wall charger",
            title="undefined"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=1.0,
            review="Advertised as UNLOCKED. It is not unlocked",
            title="undefined"
        ),

        Review(
            buyer=sarah,
            product=product,
            rating=1.0,
            review="This is good for calling and texting only.  When my child tries to use any games or anything other than basic functions it is likely to drop her application and she has to restart the device or at least the application.  This is not a negative review about this seller, just this terrible failure of a budget phone by Samsung.  My son has an even cheaper LG that can do more applications without failing.  Look for any other budget phone as it will likely be better if you want anything more than talk and text.  Battery life is the only good part of this device.  Likely because the processor is so slow it doesn't need energy.",
            title="undefined"
        ),
    ])

    # https://www.amazon.com/Galaxy-S20-5G-Unlocked-Smartphone/dp/B08FRQMW31/ref=sr_1_8?keywords=phone&qid=1673129825&sr=8-8&th=1

    product = Product(
        seller=seller,
        title="Samsung Galaxy S20+ 5G 128GB Fully Unlocked Smartphone (Renewed)",
        price="278.95",
        description="2G: GSM 850/900/1800/1900, CDMA 800/1900 and TD-SCDMA, 3G: HSDPA 850/900/1700(AWS)/1900/2100, CDMA2000 1xEV-DO, 4G LTE: 1/2/3/4/5/7/8/12/13/14/18/19/20/25/26/28/29/30/38/39/40/41/46/48/66/71, 5G: n2/5/41/66/71/260/261 - SINGLE SIM\n6.7\" Quad HD+ Dynamic AMOLED 2X, Infinity-O Display, 525ppi, 120Hz, HDR10+, 3200x1440 pixels\n128GB ROM, 12GB RAM, Qualcomm SM8250 Snapdragon 865 5G (7nm+), Octa-core, Adreno 650, 4500mAh Battery\nRear Camera: 64MP, f/2.0 + 12MP, f/1.8 + 12,MP, f/2.2 + 0.3MP, TOF, Front Camera: 10MP, f/2.2\nCompatible with Most GSM and CDMA Carriers like T-Mobile, AT&T, MetroPCS, etc. Phone will Also work with CDMA Carriers Such as Verizon, Sprint."
    )

    db.session.add_all([

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61BgDOd6ViL._AC_SL1500_.jpg"),
            preview=True,
            position=1
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/51XocCBYpGL._AC_SL1500_.jpg"),
            preview=False,
            position=2
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/51sBXTFry+L._AC_SL1500_.jpg"),
            preview=False,
            position=3
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/41YOmpsy2-L._AC_SL1500_.jpg"),
            preview=False,
            position=4
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61bWUvR8tjS._AC_SL1500_.jpg"),
            preview=False,
            position=5
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61abcuoUh0S._AC_SL1500_.jpg"),
            preview=False,
            position=6
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/51b700dO+-S._AC_SL1500_.jpg"),
            preview=False,
            position=7
        ),

        Review(
            buyer=brian,
            product=product,
            rating=4.0,
            review="The good news is this unit has not been used, so it is new old stock for 20% of new price. Bought mostly for the camera, 1/3rd the price of another Nikon. I bought the blue version, I guess that color did not sell well. It took 3 software upgrades, meaning it has been in the box since day one. I'm surprised at how clunky some of the tools are. Face recognition only works in bright light, so that's out. The phone kept telling me I'm not me, thanks loads. Hard to find the pages to change settings. No earphone jack, I had to buy some of the plug-in type. Does not sense when I am looking at it. Only 2 keyboard options, nothing for anyone with poor vision. No option for screenshots. My older much cheaper android phone by a dif maker has a LOT more ease of use features, odd. Samsung and T Mobile keep trying to install \"exciting\" games and emojis for 13 year old girls. I guess they are the primary demographic for their phones.  I wish the back is not glass, because they shatter easily. I understand why they do this, improved signal reception. The phone asked me to install facebook, when I said no it cut off the FB messenger feature. Ergo compulsory buy in on FB. I have a Samsung Gear 360 camera, I could download the app into the phone but it does not work. So good camera, poor software design, All of the basic important things work well.",
            title="undefined"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5.0,
            review="Phone works great, looks great couldn't find a scratch on the phone looked brand new. Doesn't come with phone service manual or anything like that but that's a small price to pay since can find any of that info online. Phone works great its super fast, great screen clarity. Battery life has been great also takes amazing pictures. Had S8+ which I loved but switching to the S20+ has been such a great decision. Phone very easily adapts to whatever carrier you have simply plug in your sim card and take it from there, also switching info from old phone to new was super simple, also has an option to change data from iPhone not just Android which I didn't need but if you need option is there. Fingerprints work amazing on phone even with case and screen protector on. Apps download supper fast as does everything with this phone. Would 1000% recommend the renewed phone they look amazing and for the price you can't beat it phone selling for anywhere between 750-900 elsewhere so 300 including tax you can't beat the savings. Phone is amazing I got one for myself and finance so will leave another review in few months with update on how everything is working. But as of now if you have any questions or doubts about purchasing this renewed product the only way you woukd know is that it doesn't come in an original box. Great price and best phone I've ever had. A+++++++++++++++",
            title="undefined"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=4.0,
            review="The battery does charge quick, but it does quick too. And honestly could've got all the same features on any of the galaxy series. I guess I was expecting something more from the S line",
            title="undefined"
        ),

        ReviewImage(
            review=Review(
                buyer=elizabeth,
                product=product,
                rating=4.0,
                review="I bought the phone to use outside the US and it works just fine. My only complaint is the battery. It doesn't last as I expected.",
                title="undefined"
            ),
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61aQCTOhCnL._SL1500.jpg"),
        ),

        Review(
            buyer=sarah,
            product=product,
            rating=5.0,
            review="This phone is great!  It is what you would expect.  That being said, be very careful who you buy from.  When choosing a refurbished phone only use a very reputable seller.  It is almost impossible for any seller to fully check all functions so customer support is a must.\n\nI used Hybrid IT because of their high rating and am so glad I did.  Their support was outstanding and it ended with me getting a great deal on the phone I wanted with everything as expected.  TRUST ME when you buy a refurbished phone use Hybrid IT or another seller with close to 100% feedback.  It matters!",
            title="undefined"
        ),
    ])

    # https://www.amazon.com/AmazonBasics-Performance-Alkaline-Batteries-20-Pack/dp/B00NTCH52W/ref=sr_1_2?crid=39H0ZIRVXYJ34&keywords=amazon%2Bbasics&qid=1673131349&sprefix=amazon%2Bbasic%2Caps%2C96&sr=8-2&th=1

    product = Product(
        seller=seller,
        title="Amazon Basics 20 Pack AA High-Performance Alkaline Batteries, 10-Year Shelf Life, Easy to Open Value Pack",
        price="9.89",
        description="IN THE BOX: 20-pack of 1.5 volt AA alkaline batteries for reliable performance across a wide range of devices\nDEVICE COMPATIBLE: Ideal battery for game controllers, toys, flashlights, digital cameras, clocks, and more\nDESIGNED TO LAST: 10-year leak-free shelf life; store for emergencies or use right away\nEASY USE & STORAGE: Ships in Certified Frustration-Free Packaging; easy to open and store extras for later use\nSINGLE USE: These batteries are NOT rechargeable; for rechargeable options, check out Amazon Basics rechargeable batteries"
    )

    db.session.add_all([

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/81ruqa5pXML._AC_SL1500_.jpg"),
            preview=True,
            position=1
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/81vEzLBqoHL._AC_SL1500_.jpg"),
            preview=False,
            position=2
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/612zDGeN+sL._AC_SL1500_.jpg"),
            preview=False,
            position=3
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71VLCNDupmL._AC_SL1500_.jpg"),
            preview=False,
            position=4
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/81oaBqvWAXS._AC_SL1500_.jpg"),
            preview=False,
            position=5
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71z8TgHJGDL._AC_SL1500_.jpg"),
            preview=False,
            position=6
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71RZ8Hj6JOL._AC_SL1500_.jpg"),
            preview=False,
            position=7
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5.0,
            review="I tested the AA size Amazon brand battery to find out the actual usable capacity as compared to the AA Duracell Procell battery. The results showed that the Amazon battery is about 88 percent the capacity of the Duracell. If you calculate the cost per unit capacity, the batteries are almost identical. The Amazon battery was actually slightly more expensive when represented in cost per Watt-Hour. Because of this I would probably choose the Procell (if I can get a good price on it) just because it means less frequent battery changes. The Amazon battery is a surprisingly good battery though. You will probably barely notice the difference in capacity, so if you don't want to waste time shopping around then its a good choice.\n\nI also performed the same test on Duracell Copper Top, and Energizer Max. Their performance was nearly identical to the Procell. More interestingly, I tested the Energizer Ultimate Lithium AA cell. This cell was 4 times the cost of a procell at $1.27 per cell! However the capacity was only 1.5 times that of the Procell. So don't waste your money on these batteries, they're much more expensive per unit of capacity. The capacity of all these batteries were measured in Watt-Hours. Here are the numbers.\n\nAA Amazon Battery = 2.71 Wh. My cost per cell = $0.291. Cost per Watt-Hour = $0.107\nAA Duracell Procell = 3.09 Wh. My cost per cell = $0.321. Cost per Watt-Hour = $0.104\nAA Energizer Lithium = 4.86 Wh. My cost per cell = $1.27. Cost per Watt-Hour = $0.261\n\nThis test was done using an op-amp circuit to maintain a constant current load at 100ma. Voltage and current were being logged ounce per minute and this data was used to calculate the Amp-Hour with a 0.8 volt cutoff. The Watt-Hour was then calculated by multiplying the Amp-Hour by the average voltage from the beginning of the test to 0.8 volts. All batteries mentioned were tested using this same method. Note that the capacity of these batteries can change dramatically under different conditions. The same battery under a heavy load will have a fraction of the capacity that it would under a light load. This data is only good for a comparison when choosing what battery is worth buying at what price. Unless your device loads the battery at a constant current of 100ma.\n\nIn summery, the Amazon batteries are not bad batteries (at least based on this test using the AA cell). If you choose to shop around for a name brand battery, stay at or below $0.33 per cell. Anything above $0.33 per cell will be more expensive per unit capacity than the Amazon battery. Oh, and definitely stay away from the Energizer Lithium unless expense is not an issue. These batteries are only worth the additional cost if your application requires a light weight and relatively high capacity battery regardless of cost. These batteries are surprisingly light weight compared to an alkaline.lkaline.",
            title="Results of capacity testing shows its slightly below the competition."
        ),

        ReviewImage(
            review=Review(
                buyer=caitlynn,
                product=product,
                rating=5.0,
                review="Like many of us after the holidays, I found myself short on AAA batteries. Well, actually…I was totally out of them after all the wreaths and trees with lights and remotes I had for the holidays.\n\nAfter hunting around and comparing prices, this Amazon Basics purchase seemed to be pretty cost-effective.\n\nI received the shipment pretty fast and was impressed with the packaging. I like how these batteries came in a sturdy box and the batteries were sealed in plastic in four equal portions. I opened the first package to keep in my battery container and will keep the others sealed until it’s time to break them open. I like to keep batteries on both floors of my home for convenience.\n\nI also like that they have a shelf life of ten years, though I don’t think it will be that long before we use them.\n\nThe batteries I have used so far had a full charge. I always keep a battery tester with my battery stash, so I can see what the charge is.\n\nI am very pleased with this purchase and feel that it is a good value. I will be looking to buy Amazon batteries again in this and other sizes.",
                title="This is a pretty good deal for batteries"
            ),
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71J73LiVr7L._SL1500.jpg"),
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5.0,
            review="I had been using several brands of batteries, and they never seemed to last very long. My home devices need AA batteries, so I am using these Amazon's Alkaline Batteries for my remotes, flashlights, and smoke detectors to see if they live up to their efficiency. I find this 20-pack set the most practical because the batteries protect your devices from leakage, and I don't have to worry for a while once I use them. They are aimed at high demand and are advertising to last 50% longer than other store-bought batteries. It also has a 10 yr shelf life, so you can have them around in case you need them. The packaging they came in is what you expect from Amazon; well-received and in excellent condition. They're my go-to batteries from now on. Highly recommend!!!",
            title="Super Long Lasting AA Batteries :-)"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5.0,
            review="For many uses, I prefer Amazon Basics rechargeable batteries, but there are some situations where the device isn't happy with the voltage profile of a rechargeable (typically 1.2 volts) compared to an alkaline (typically 1.5 volts to start).  For the majority of those situations, AC Delco are my favorite low cost AA alkaline batteries, but, they were not available, so I went with these Amazon Basics which were only slightly more expensive the AC Delco.\n\nFor typical uses like the many, many, LED candles and mini-Christmas tree lights my wife has scattered around the house, these provide a cost effective solution.\n\nThe only use for which I have found that these aren't ideal is in our smart lock.  For this use, I find that Duracell batteries outperform value batteries, providing over twice the life.  But, since the Duracell cost twice as much as the these, it isn't a cost thing, it's more the convenience of not having to change the batteries as often that leads me to use the Duracells for the smart lock.\n\nThe one minor complaint I have with these Amazon Basics batteries is the packaging. They do provide a slight challenge to get out of the shrink wrap.",
            title="Good relatively low cost AA alkaline batteries"
        ),

        Review(
            buyer=sarah,
            product=product,
            rating=5.0,
            review="The Amazon Basics 100 Pack AA Batteries are an excellent choice for powering your everyday devices. They are reliable, long-lasting, and provide consistent power. The batteries are made with high-quality materials and are designed to last up to 10 years in storage. They are also leak-proof and have a low self-discharge rate, so you can be sure that your devices will stay powered for a long time. The batteries are also reasonably priced, making them a great value for the money. Overall, the Amazon Basics 100 Pack AA Batteries are an excellent choice for powering your everyday devices.",
            title="For The Price  - Can't beat it!!!"
        ),
    ])

    # https://www.amazon.com/Amazon-Basics-microSDXC-Memory-Adapter/dp/B08TJRVWV1/ref=sr_1_5?crid=39H0ZIRVXYJ34&keywords=amazon%2Bbasics&qid=1673131349&sprefix=amazon%2Bbasic%2Caps%2C96&sr=8-5&th=1

    product = Product(
        seller=seller,
        title="Amazon Basics microSDXC Memory Card with Full Size Adapter, A2, U3, Read Speed up to 100 MB/s, 128 GB",
        price="14.59",
        description="Make sure this fits by entering your model number.\nWIDE COMPATIBILITY: Compatible with smartphones, tablets, cameras, GoPro/action cameras, laptops, desktop computers, DSLRs, drones, Nintendo Switch/other portable consoles and much more. Includes SD adapter. Note: Please refer to compatible devices list (keep update) in below Product guides for more detail.\nHIGH QUALITY STORAGE: Perfect for high resolution photos, for recording and storing Full HD/4K videos and any other data type\nULTRA FAST: Read speed up to 100mb/s. Write speed up to 60mb/s (varies according to memory size). UHS, U3, Class 10 and A2 speed classes for an optimal smartphone experience\nLASTING RELIABILITY: Shockproof, IPX6 waterproof, temperature-proof (-10° to 80°), X-Ray-proof and magnetic-proof\nNote: Actual storage capacity shown by a device's OS may be less than the capacity indicated on the product label due to different measurement standards. The available storage capacity is higher than 116GB.\nRead and write speeds are based on internal tests conducted under controlled conditions. Actual speeds may vary depending on device used, interface, conditions of use, and other factors\nNote: Please note that we are changing the product's printing and packaging; both 2 versions are the same. (Old version does not show the A2 logo, but its performance is A2 level.)\nNote: Check whether your device is compatible with the MicroSD capacity, for example, if the device only supports a maximum capacity of 64GB, it may not recognize 128GB MicroSDs above"
    )

    db.session.add_all([

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61DwejyTGkL._AC_SL1500_.jpg"),
            preview=True,
            position=1
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71swf31eHtL._AC_SL1500_.jpg"),
            preview=False,
            position=2
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/81odhbhx3BL._AC_SL1500_.jpg"),
            preview=False,
            position=3
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/818qMd1TCDL._AC_SL1500_.jpg"),
            preview=False,
            position=4
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/81E2vgO9vmL._AC_SL1500_.jpg"),
            preview=False,
            position=5
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/815qkPHsGZL._AC_SL1500_.jpg"),
            preview=False,
            position=6
        ),

        ReviewImage(
            review=Review(
                buyer=brian,
                product=product,
                rating=5.0,
                review="I am reviewing and comparing two different memory cards, the Amazon basics 256gb and the SanDisk Extreme 256gb card.\n\nFirst is price, the Amazon basics is a several dollars less than the SanDisk (at this moment 23.72 vs 36.99). Currently Amazon says there is a newer version of the SanDisk for 24.85, however I have not purchased or tested the newer version.\n\nThe two cards:\n\"SanDisk 256GB Extreme microSDXC UHS-I Memory Card with Adapter - Up to 160MB/s, C10, U3, V30, 4K, A2, Micro SD - SDSQXA1-256G-GN6MA\"\n\"Amazon Basics microSDXC Memory Card with Full Size Adapter, A2, U3, Read Speed up to 100 MB/s, 256 GB\"\n\nTested using:\nCrystalDiskMark 5.5.0 x64.\nComputer is a 4 year old \"NUC8i7HVK\" running Windows 10, and it has a built in SD card reader (Intel calls it \"SDXC with UHS-I support\"). This interface is what I call \"SD reader\" in the accompanying screen captures.\nI also tested using a SanDisk USB 3 adapter \"SanDisk MobileMate USB 3.0 microSD Card Reader- SDDR-B531-GN6NN\". This interface is what I call USB3 in the accompanying screen captures.\n\nFirst, I noticed a UK review where the reviewer noted the Amazon basics card seems to be missing 5 gigabytes of storage even when the (confusing) translation from computer storage gigabytes (1024 x 1024 x 1024 = 1,073,741,824 bytes vs 1000 x 1000 x 1000 = 1,000,000,000 bytes) vs \"we sell storage\" gigabytes. You will notice CrystalDiskMark reports the Amazon basic card as 233GiB versus the 238GiB of the SanDisk, so he is very correct. I have no clue why the discrepancy, but it is slightly smaller than it should be.\n\nSecond, to get the real read/write speed of the SanDisk card, you will notice I had to use the SanDisk USB 3 adapter. Using the built in SD card reader, both cards were very close to identical results.\nUsing the SanDisk USB 3 adapter, I did manage to exceed the ratings for the SanDisk card (up to 160 MB/s read, and up to 90 MB/s write) giving 169 read and 105 write. The Amazon basic card did have a slight change using the SanDisk adapter, but really not significant.\n\nBoth cards were close enough to their claimed specs to not worry about it, however it should be noted that you need the SanDisk adapter to actually get the much higher speeds of the SanDisk.\nI will be using the Amazon basic card to store children's movies for my granddaughter to play on her new Kindle, it is plenty fast enough reading to do full HD movies.\n\nNote that both cards were brand new when tested and had never had anything written or read from them prior to the test. The Amazon basic seems a good value and is certainly adequate for normal use in a cell phone or laptop. The SanDisk would really shine if you used the adapter to move lots of larger files to it.",
                title="256gb Amazon basic vs 256gb SanDisk Extreme"
            ),
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61MWGEaPvBL._SL1500.jpg"),
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5.0,
            review="I'm a sucker for a bargain and always trying out Amazon Basics branded items when I need them. They're almost always a great value. But even I was still hesitant about them hawking cheap Mirco SD cards. Especially with these specifications, features and advertised speeds. But here I am, fully satisfied and impressed. They deliver.\n\nI figured that worse case scenario I'd use them on less demanding gadgets. But you can slap one of these in something like a Steam Deck, install a AAA game, and notice no difference from a quality line of name brand cards. Now maybe the quality control is lower, and/or maybe they have shorter lifespans. But I bought two 256gb cards and both work fine. On anything from gaming devices to tablets to cameras and so on. Transfer speeds are there in both read and write. No reliability issues at all. I've had no issues with data loss in mounting/unmounting. And they've been holding up so far.\n\nWith so many gadgets these days using the Micro SD format I'm starting to have quite the collection. I've got stuff like Samsung EVO Select's and Pro's. And then I've got stuff all the way on the other end of the spectrum like unbranded generic ones that die the first time you eject them from the device they came with. I am very comfortable in saying that these are performing for me like the Samsung's on the higher end of the spectrum. With the prices these go on sale, there's no reason not to add them to your mix. You can always use them in less important or demanding devices if you don't want to trust them. But like I said, I'm using them in demanding devices with regular heavy use and they're up to task.\n\nDefinitely recommend them.",
            title="Color me Impressed"
        ),

        ReviewImage(
            review=Review(
                buyer=derrik,
                product=product,
                rating=5.0,
                review="I used this for a dash cam and the camera had no problem formatting the card the adapter makes it easy to take it out then watch the clips on my computer. I only use this to store videos but it has the full capacity stated when my dash cam checked",
                title="Best deal for price"
            ),
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/614YUnqpyiL._SL1500.jpg"),
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=4.0,
            review="I ordered this because the price was very reasonable, and I know most Amazon branded products are good quality. I needed another 128gb card to \"clone\" one that has a specific functioning program on it for one of my small form factor computers so that I can put the second cloned card into my second identical computer that doesn't want to function correctly with a NEW install of the same software. The problem is, the working 128gb card reads as 119gb, and the new Amazon 128gb card reads as only 117gb so it is too small for cloning the working one. It's not that the card doesn't work, or isn't any good, it is just smaller than it needed to be, which is very disappointing. I now have to get another card of a larger formatted size for this project. The Amazon card is working just fine however in my sons Nintendo Switch, so I can't complain too much. If you're looking for a slightly undersized 128gb micro sd card at a very reasonable price, and can live with only 117gb, buy this one and you'll be happy you saved a few bucks. I'd buy it again for other projects, or for a dashcam, gopro style cam, or maybe for security cameras, or maybe a tablet/phone, because they would be fine for those uses.",
            title="Disappointed in this one"
        ),

        Review(
            buyer=sarah,
            product=product,
            rating=5.0,
            review="Went to the store and saw they were charging $13 for 32 gigabytes but then I go on Amazon and I can get 120gb for the same price! I bought this SD card to use on my dash cam and it’s worked perfectly so far.",
            title="Best SD Cards Out There"
        ),
    ])

    db.session.commit()


def undo_seed():
    db.session.execute("TRUNCATE TABLE users RESTART IDENTITY CASCADE;")
    db.session.execute("TRUNCATE TABLE products RESTART IDENTITY CASCADE;")
    db.session.execute(
        "TRUNCATE TABLE product_images RESTART IDENTITY CASCADE;")
    db.session.execute("TRUNCATE TABLE reviews RESTART IDENTITY CASCADE;")
    db.session.execute(
        "TRUNCATE TABLE review_images RESTART IDENTITY CASCADE;")
    db.session.commit()
