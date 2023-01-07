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

    # https://www.amazon.com/AquaSonic-Black-Ultra-Whitening-Toothbrush/dp/B072YVWBXH/ref=sr_1_7?crid=234FOMCTX8NL8&keywords=electric+toothbrushes&qid=1673123804&s=hpc&sprefix=electric+toothbrushes%2Chpc%2C286&sr=1-7

    product = Product(
        seller=seller,
        title="Aquasonic Black Series Ultra Whitening Toothbrush – ADA Accepted Power Toothbrush - 8 Brush Heads & Travel Case – 40,000 VPM Electric Motor & Wireless Charging - 4 Modes w Smart Timer",
        price="39.95",
        description="40,000 VPM Smart Toothbrush – Beauty, brains and power. The Black Series is a world class modern electric toothbrush packed with the most up to date technology. It features an ultra-powerful and industry leading motor producing 40,000 vibrations per minute, a lithium-ion battery, ultra-fast wireless charging, 4 mode operation, smart vibration timers, 8 DuPont engineered brush heads, and a custom travel case; all with a sleek ultra-slim, lightweight and IPX7 rated waterproof design.\nAccepted by the American Dental Association (ADA) Council on Scientific Affairs – We put our money where your mouth is. Investing in premium oral care technologies has earned the Black Series the prestigious ADA seal of approval. It has shown efficacy in removing plaque and helping to prevent and reduce gingivitis. Black Series goes beyond just cleaning teeth – it provides complete oral care with unique modes that include one for whitening and polishing teeth, and one for improving gum health.\nModern Tech for a Healthy Smile - Black Series brings toothbrushes into modern times with its built-in enhanced features. A lithium-ion battery, ultra-fast wireless charging (forget outdated USB charging), 4 distinct brushing modes and a smart vibrating notification timer are some of the enhanced features built into the sleek and ergonomic waterproof black satin handle.\n8 DuPont Brush Heads & Travel Case Included – Included are 8 brush heads engineered by world famous DuPont; a world leader in quality & materials science. Each brush head lasts 3-4 months so 8 will last for about 2.5 years. Also included is a convenient custom hard shell travel case made of BPA-free plastic with space for two brush heads. Black Series can last 4 full weeks (2 min/2x a day) on a full charge so it's perfect for on the go travel with the included travel case.\nWhat's in the Box - 1 AquaSonic Black Series Smart Toothbrush, 1 wireless charging base, 8 DuPont brush heads, 1 travel case, warranty card, and user manual."
    )

    db.session.add_all([

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/716hFx-iA3L._SL1500_.jpg"),
            preview=True,
            position=1
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61avUWWlfVL._SL1500_.jpg"),
            preview=False,
            position=2
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71SOw28551L._SL1500_.jpg"),
            preview=False,
            position=3
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71oarZSrQmL._SL1500_.jpg"),
            preview=False,
            position=4
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71F+l2UuFtL._SL1500_.jpg"),
            preview=False,
            position=5
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/81a4msVETbL._SL1500_.jpg"),
            preview=False,
            position=6
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5.0,
            review="bought june 2022 mow early dec\nusage is about 1 to 2x a day as i have oral b 1000 costco item\nbattery at gentle speeds with 1 to 3 full 2 minute sessions at a time each day will last TWO (2) months!!!!!!\ntake that you over priced oral b! which barely lastrs 7 days with 2x sessions each at 2 min.\n\nthe aquasonic will clean well\nstill find oral b simpler as i dont have to actually 'brush' with OB as it does all the work for me\nbut AqS works at what i does and does better with rear molars esp the space between back two molars on each end of mouth (as in the lat two moalrs on each side of jaws)\n\ndownside? again wish it had slipperly reg plastic body w/o the soft touch coating. those eventually over time will degrade n become nasty sticky icky mess but...maybe thiers will notdos. if it does then ill just use adhesive remover\n\nthe oral b had 50 percent faiure rate as i bought 2pack from costco after 1 year, one failed to charge\nso time will tell if AaS is more durable and long lasting. i really hope so as it is is cuh a g8 value\n\n8 brush heads from ob? 60usd.\nfrom AqS? incld wih $40 toothbrush! that is 2 years of brush heads included!\n\noh i guess this is a downside but also could be how this thing lasts so long on a charge - you n need to charge 24 hours to get full 100% charge\n\nbut at same weight and zie as ob, not sure what kinda battery it uses but clearly far far far far superior to oral b\n\nthanks AqS!\n\nSorry for my typos! lol\n\nbottom line: buy this toothbrush\n\nAUg 31 2022 update\napprox usage 1-3 full cycles (2 min each cycle) daily\nstill havent had to charege the battery!!!!\non weekends, sometimes i have used it 3x a day with 1 - 2 ful lcycles\nmy oral b battery? horrible. lasts barealy a week without charging using 2x a day 1 cycle per usage. i keep it on charger most days\n\ncomparison:\nAS:\nsofter bristles\nlittle harder to get fully clean teet IMO as still havent gotten used to how to use it properly\namazing battery life - the review that said husband/wife use just one AS while switching brush tips, and it lasting for months, is not a lie. it is true i tell. true lol. i know cuz mine i have only done ONE 1x full 24 hour (which manual directs you to do - 24 hour for full charge). ive done that 1x back when i bought it.\nno weakening of power and its now aug 31th!\nsame size as Oral B housing yet AqZSn battery is clearly much bigger and of much higher quality than Oral B\nPrice for Aq includes 8 brush heads!\ni dont know if Azmn sells AqSn brush heads but i wont have to do so for a long time. 8 w each lasting 3 months would be 2 years worth of brush heads! and the price included the toothbrush!\nso while i do prefer easier brushing with OB, the AS is clearly a far better value and far better battery quality\nas one reviewer mentioned the AqSn brucsh head breaking, i am ultra gentle with my brushing to prevent that from occuring (i hope). tehoretically, same issue could occur with any of these electric toothbrushes\n\nCons:\nno power level indicator like OB has 3 leds for pwr. i wish AqS had this but as i said, im still on original charge 2 moths of usage !!! so the con is nitpicking lol\nstill havent really firgured out if i am brushing properly  but i have same issue with a manual toothbrush lol\nbottom line:\nthe AS is superior to a reg toothbrush (by how much i dont know). i use level 2 power (not the max) and it seems to work well even with my feather light brushing of teeth\nwaterproof esseentially - iave rinsed entire housing repeatedly just like with my Oral B, neither has had issues\n\nthe one future con i foresee:\nthe brush head has a matte finish and all matte finshess become disgusting stickiy over time. i basiclaly will need to remove the matte finish at some point using heavy duty  adhesive remover but that is oky.\n\nthe oral b does not have a matte finish which is batter.\n\nOral B\npoor battery life\nEXPENSIVE brush heads 55 for 9!\nexpensive to replace when battery eventually dies at 50 usd\nfloss action - these are the specific heads i use and they work great cuz they cover whole tooth\neasier to use than AquaS. as i simply hold over each tooth and let OB do the work\nSTIFF bristiles though\noverall OB cleans better IMO\n\nJune 26 2022\nonly used 1x just initial impressions will update later\n\nive used oralb 3d series from costco for 2 years using their floss action head\npros of OB is effortless - all ii have to do is hold the brush feather lightly agasinst teeth vertically - not movement needed like standard toothbrush\n\nAquasonic Sonic Toothbrush has an accurate title which means it is a toothbrush with a sonic function.\ni have no idea if this sonic function 40k bpm actually does anything....\ni was hoping for a $30 oral-b replacement but instead it is a standard toothbrush with a sonic funciton meaning i stilll have to brush my teeth like a normal toothbrush.\n\nwhine whine whin i konw ha ha ha\nbut i have i bone spurs in shoulders blades where upper movent causes pain hence my preference for oral b no effort tootbrushing over aquasonic.\n\ni will stil keep and use aquasonic as as a backup to my oral b\n\nwill update later once ive used long term\n\nbut again, best value for money for a toothbrush with sonic function...but again...does it actually remove plque better than standard ultra soft tootbrush???? i konw ora-b floss action head does work better but does aquasonic????\n\ntime will tel.... will update later and sorry for typos",
            title="5 month update"
        ),

        ReviewImage(
            review=Review(
                buyer=caitlynn,
                product=product,
                rating=2.0,
                review="The image included with this review is to provide a reference point for review. My previous e-brush is a sonicare g2 series (nowadays i found i can interchange the heads for different series, as the brush i have allows for most features present in other devices). the sonicare cost me around $50-60 (can't really remember) at the time of purchase (around four years ago, which speaks to sonicare's longevity). the brush still works well, i will add, just that i don't like the price point for replacing the brushhead, and nowadays i have noticed a slight reduction in speed and battery longevity (although mostly i just wanted to try something new after four years of the same brand).\n  i heard about this aquasonic with the significantly reduced brushhead pricepoint (i buy my heads at Costco at 2 for $18 before taxes, whereas aquasonic comes with 8 brushheads at $34.99 for the entire set, including brush and travelcase). Overall, I would say I am VERY impressed with the Aquasonic. I have tried Oral-B and other brands that have came and went throughout the years (i found that sonicare had softer brushes and the overall experience was better for me), so I have a decent general idea of what's out there. I have had the item for a weej and will try to update periodically as i know ebrushes are a significant investment for some (especially families) that are new to the experience, and it can be difficult to trust reviewers nowadays.\n  Here are Pros and Cons:\nPros\n  The smooth matte-like feel of the brush (which surprisingly no one talked about in the reviews i read), which immediately caught my attention. it makes me WANT to use the brush.\n  The lightweight feel of the brush in my hand. It is actually noticeably lighter than my sonicare, which i already loved for how lightweight it was.  For the price, this was one of the shockers.\n  The SOFTNESS of the brush itself. Some reviewers noticed the small size (this tells me they probably haven't had an ebrush before because some dentists online actually say a smaller size is ideal for greater teeth coverage), yet as you can tell it's about the same size as my sonicare (if not slightly bigger). I have senaitive teeth and my dentist keeps telling me the apfter the better. i legit didn't think there was an ebrush softer than my sonicare (the g2 series is designed specifically to be soft). again, for the price point, another shocker.\n  The mode selection text. This might seem obvious, yet most ebrushes i have used in the past only have a light that blinks and tells you the mode you're on in a more subtle way. i was indifferent to this feature as i want to believe i am smart enough to understand the blinking system and the vibration of the brush to understand which mode i am in, however, i have to admit it definitely makes it easier and to my taste does not remove any points in the aesthetics department.\n  the cleaning power. this also shocked me a bit because, again, for the price point this brush works as well if not better than my sonicare. there's also a noticeable difference between each mode, compelling me to believe that the other modes are just as effective in their intended purpose (i have only tried the massage and clean modes, and they do what they say they'll do).\n  the attachment process. the setup is the same as my sonicare (to the extent that i wouldn't be surprised if this company used the sonicare design as inspiration, because it is pretty similar\n in key areas yet surprisingly better overall, in my opinion, so far), with the head attaching to the base of the brush with a simple push and pull feature.\n  the two button difference for power on/off and mode. this definitely tells me they hsve learned from the user experience in other brushes because that has been one of my pet peeves— one button to select them all with only the blinker to guide you. the peeve is mostly with the time consumption (as some ebrushes require a hold in order to change modes or to change quadrant features). this brush also has quadrant features that seem more fluid than my sonicare.\n  i will also give points for aesthetics, as the entire setup looks well-thought out (as in, they probably just got the better features of other ebrushes and went with that 😂 ).\n  the travel case. the sonocare comes with brushhead cover, which i actually love for its simplicity and utility, yet the idea of a cover somehow feels more thoughtful (even though the head cover is actually more functional).\n Cons\n  i don't know yet (just a week in).\n  i will update as i go to podt any issues. i got the 3-year insurance due to how cheap it was and the fact that if this covers me for 3 years, it will automatically make it as long-lasting as my sonicare (even better, considering sonicare warranty only covered me for one year).\n  i will say this— i LOVE my sonicare and am in no way bashing. if you want a durable, quality brush, go with sonicare (i will vouch for them).  Phillips (the parent company of sonicare) is well known for their quality products, yet lately i have noticed better price points elsewhere. at some point the drop in price overwhelms the quality, as long as there is a base function that's being met. So far this aquasonic is merting that base function, and some. if this continue for as long as the warranty is covered, i definitely can say i am going with aquasonic in the future. i am also content with knowing i don't have to worry about a trip to the store for a replacement head for at least two years (i was starting to dread having to get new replacements for my sonicare with greater frequency, as i can almost say that the color indicator on the brush keeps getting shorter and shorter in lifespan lately). this will be my best reason to get the aquasonic, as i don't like it when a company uses Rockefeller tactics (we're in 2021, and those tactics were conceived of in the 1920s).\n###\n\n***UPDATE--- One Month After Purchase***\n  So, the previous review was not bad on the Aquasonic, yet after a while of only using this bruah I started to notice that there was starting to show some plaque build-up on my teeth. This was confusing because my Sonicare isually took care of any buildup quite easily, and most other legit ebrushes have a similar capacity. I started to think maybe I wasn't brushing 'right' yet that didn't make sense because I have been brushing about the same for either brush. Thankfully I didn't toss my Sonicare, because, as previously mentioned, it still worked just fine after four-five years of use.\n  Well, whay do you know? The Sonicare took care of the plaque with ease (which was a relief because after a while it is nearly impossible to remove plaque on teeth and I have to wait for biannual checkup to have a hygienist do it, which can be a bit embarrassing but that is what they do so whatever). Someone else on another review mentioned how Aquasonic was a bruah that just vibrated and did nothing. Well, now I know what they mean.\n  This brush is amazing for decorative purposes, yet is you want to save yourself a trip to the hygienist, get a quality, reputable brand. As with anything, you pay what you get. I especially appreciate the Sonicare took care of in-between teeth plaque as well (for those of you who don't know, you van 'feel' plaque on teeth when you feel something rough on the surface of teeth. Your teeth are naturally smooth and feels good when the tongue glides over a set of clean, plaque-free teeth. Also, there is a chemical agent provided by my hygienist for checking for plaque, which can be expensive and only meant to be used periodically and not even weekly.).\n  Well, that was a waste of $40+tax.\n  For thise whi might say, 'Well, you just have to brush harder or provide more motion', I say this— that is the whole point of an ebrush, that you don't have to do much and the brush does all the work for you. If I have to put in work, it's a manual brush (which I also have for travel/work and emergencies when I forget to pack my ebruah for travel, and there's nothing wrong with using a manual brush other than that in my experience a good ebrush will keep your teeth as plaque-free as possible). That defeats the whole point of buying an ebrush.\n  This Aquasonic looks great and feels great, yet it doesn't perform its stated function. That's like a beautiful car that doesn't drive, you have to push it yourself. It looks beautiful and aggressive, like it can go fast, yet ultimately it doesn't go anywhere. It doesn't perform its intended function (unless you're the kind of person that likes to spend money on decorative vehicles, which I am sure is a niche market rhat does exist). Please be advised of this, as it mifht save you a visit to a hygienist (you go to your dentist twice a year but sometimes even dentists don't have the specialist experience to clean and polish teeth like a hygienist, which sometimes requires special equipment that uses water, air, and baking soda at once.). I was abke to experiment and now am probably going to have to visit my hygienist anyway, but I was willing to take that risk. I understand not everyone has the cash to take that risk, so be warned.",
                title="Unexpectedly Great, Until It Isn't. Buy Reputable Quality Instead."
            ),
            url=upload_image_to_bucket_from_url(
                "https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif"),
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5.0,
            review="Simplemente wow. Es mi primer cepillo eléctrico y sinceramente me quedo con un sabor de boca buenísimo (literal). No lo he cargado desde que me llegó hace 15 días y sigue funcionando, supongo que así será por 15 días más. No es abrasivo (cuidado con la presión al cepillarte, porque no requiere de tanta) y realmente queda muy limpia la boca después de un cepillado de 2 minutos. Trae temporizador integrado (deja de vibrar por 1 segundo para que te pases a otra área de la boca) y generalmente no le pide nada a un Phillips Sonicare. Buena compra 10/10",
            title="Un cepillo eléctrico excelente"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5.0,
            review="",
            title=""
        ),

        Review(
            buyer=sarah,
            product=product,
            rating=5.0,
            review="I bought this for my husband as part of a gift because his oral B would no longer hold a charge. He was so over the moon about it after the first use that I thought surely he must just be trying to act over the top about the gift. He still wouldn’t shut up about it months later. We went away for a weekend and I forgot my toothbrush and he suggested I use the extra brush attachment that he has in the case and use it. I threw my oral B out. I have never ever experienced a toothbrush that did a better job that this. My husbands dentist praised him for his flossing when he rarely flosses. My teeth are whiter than they have ever been and I can only compare how clean my teeth get to the cleaning I get at the dentist when I get the good hygienist. I’m blown away. My husband was not exaggerating at all. Now I just have to buy my own. I’m still using his spare brush head. The case comes with two heads and plus you get 6 other spares too so 8 brush heads total. My husband hasn’t charged it since mid February and still going strong. I’m going to chuck my kids oral B’s and get them these. They would be fantastic for brushing braces. The vibrations get in every nook. Bravo!!",
            title="Amazing in every aspect!"
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
                "https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif"),
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

    # https://www.amazon.com/Electric-Toothbrush-Adults-Travel-Rechargeable/dp/B09NSTXLK1/ref=sr_1_18?crid=234FOMCTX8NL8&keywords=electric%2Btoothbrushes&qid=1673124949&s=hpc&sprefix=electric%2Btoothbrushes%2Chpc%2C286&sr=1-18&th=1

    product = Product(
        seller=seller,
        title="PHYLIAN Sonic Electric Toothbrush for Adults and Women - Rechargeable Electric Toothbrush with 8 Brush Heads, Travel Case, Sonic Toothbrush 3 Hours Fast Charge for 60 Days - Pink, 1 Count (Pack of 1)",
        price="27.99",
        description="Whiten your Teeth: PHYLiAN sonic electric toothbrush for women whiten your teeth in 14 days by powerful sonic technology\nClean 3X More Plaque With A High Power Toothbrush: This electric toothbrush for teens with 40,000 high-frequency vibrations per minute, more effective than the average low-frequency oscillating electric toothbrush\n120 Days Use/Charge + 24 Months of Use: This rechargeable toothbrush for adults can be used for 120 days per 3-hour charge and comes with a portable travel case, perfect option for travel. 8 premium DuPont toothbrush heads will last 24 months, saving your money for change new elcctric toothbrush\n5 Modes for All Oral Care Needs: Use the pink electric toothbrush set for adultsdaily for plaque removal, choose whitening mode to remove stains from the teeth, select sensitive mode to protect your gums, massage your gums, or polish your teeth before an appointment.\nDevelop Healthy Tooth Brushing Habits: Built-in 2 minutes timer to ensure scientific brushing time, the power sonic toothbrush for adults pauses every 30 seconds to remind you to change the brushing area.\nCONTACT US：Login your amazon account > choose \"Your orders\" > find the order ID > click \"Contact seller\". PHYLIAN brand promise 12 months after-sale service and friendly customer service such as within 24Hrs response E-mail support for troubleshooting, telephone customer service."
    )

    db.session.add_all([

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71mk1WSjsoL._SL1500_.jpg"),
            preview=True,
            position=1
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/71r4fsw4HJL._SL1500_.jpg"),
            preview=False,
            position=2
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61zz1jlwRdL._SL1500_.jpg"),
            preview=False,
            position=3
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/61UATNj3k+L._SL1500_.jpg"),
            preview=False,
            position=4
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/612i85KHJ9L._SL1500_.jpg"),
            preview=False,
            position=5
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5.0,
            review="I wasn't sure about purchasing this toothbrush because of the low price. I have been using it for about a month now and am so glad I took a chance on it. It leaves my mouth feeling fresh from the dentist office clean. My teeth shine. I like it so much I bought one for my husband. It's great that there are so many colors to choose from. Mine is pink and my husband's is black so we will never mix them up. Also the brush comes with several replacement heads which is awesome. My daughter's electric toothbrush did not come with any replacement heads and she has to buy a replacement head every three months. So far I am very pleased with this purchase. If something changes as it ages I will update.",
            title="I love my new toothbrush!"
        ),

        ReviewImage(
            review=Review(
                buyer=caitlynn,
                product=product,
                rating=4.0,
                review="This is my first electric toothbrush. I had to make the switch because my gums are sensitive and apparently I over brush/brush too hard so the dentist recommended an electric toothbrush. For what this cost, I’m not disappointed. It came with plenty of replacement brush heads,  was neatly packaged, and has a slender travel case. I also like that the toothbrush has a “sensitive” setting AND the fact that it stops after 2 minutes of brushing , which is awesome. I’m still getting used to it but I’m not disappointed. I’ve been too nervous to let it completely die so I’m not sure how many days/uses the battery lasts.\n\nThe one thing I dislike is that it randomly “pauses” in the middle of use. I originally thought it paused to give guidance of when to switch up where you’re brushing but I don’t really think that’s it. Anyway, it’s a good product and will likely use it until it dies as there are no major reasons i need to stop using it.\n\n*UPDATE*\nLess than 30 days after purchasing this toothbrush and it has broken. The random pauses I mentioned before began to be longer and longer and eventually died last night. The light turns on but it won't vibrate at all. This started maybe a day or so ago so I charged it, even though it had a good charge to it and when it would 'pause', I had to tap the brush before it would start working again but when I used it this morning, it wouldn't vibrate at all. Will be requesting a refund.",
                title="Great for the price - UPDATE BELOW"
            ),
            url=upload_image_to_bucket_from_url(
                "https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif"),
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5.0,
            review="The battery life on this brush is pretty long lasting. Super easy to travel with as it has a travel case. Every thirty seconds it has a little pause and then stops automatically at the 2 minute mark. I usually just turn it back on to continue brushing if I want or need, so not a biggie. I like it so much I got one for my fiancé and he likes it as well. We feel it does a great job of making our teeth feel clean. It comes with brush replacements, but I have not been able to find addition replacements for when these run out. Hopefully the become available soon or maybe I am just missing them?",
            title="Love this toothbrush"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5.0,
            review="THIS TOOTH BRUSH IS PHENOMINAL!  I LOVED THE COLOR OPTIONS, WITH TRAVEL CASE. CAN USE ANY PHONE CHARGER TO CHARGE IT!  IT COMES FULLY CHARGED, AND THE CHARGE LASTS FOR UP TO 60 DAYS!!!!!  THE MOST IMPORTANT FEATURE OF THIS TOOTH BRUSH IS, IT HAS  5 CYCLES. IT HAS A CLEANING CYCLE, WHITENING CYCLE, POLISH CYCLE, MASSAGING CYCLE FOR YOUR GUMS, AND A SENSITIVE CYCLE FOR SENSITIVE TEETH, OR IF YOU MAY BE HAVING DENTAL WORK DONE! IT'S LIKE SENDING YOUR TEETH TO A SPA! I FIRST BOUGHT THIS TOOTH BRUSH FOR MYSELF IN PINK. I ENJOYED IT SO MUCH SEEING RESULTS AFTER TWO DAYS, I BOUGHT A SECOND TOOTH BRUSH IN BLACK FOR MY HUSBAND. BY THE TIME I PURCHASED HIS TOOTH BRUSH IT HAD BEEN REDUCED IN PRICE ALMOST BY $10.00.  I WANTED HIM TO HAVE THE SAME SPA LIKE EXPEREINCE FOR HIS TEETH AS I DID. EACH CYCLE IS A 2 MINUTE CYCLE, REMINDING YOU EVERY FEW SECONDS TO MOVE ON TO ANOTHER AREA OF BRUSHING!  I HAVE RECOMMENDED IT TO ALL OF MY FAMILY &amp; FRIENDS!",
            title="ELECTRIC TOOTH BRUSH WITH 5 CYCLES!"
        ),

        Review(
            buyer=sarah,
            product=product,
            rating=5.0,
            review="Buying a second one now for myself! I bought one for my fiance back in October and he's only had to charge it about once a month because the battery life lasts forever! It also does an amazing job at cleaning your teeth. My current toothbrush oral b needs to be charged all the time so I'm swapping it out for one of these!",
            title="Highly recommend! Buying a second one now"
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
