from app.models import db, User, Product, ProductImage, Review, ReviewImage
from app.seeds.upload import upload_image_to_bucket_from_url


def seed_all():
    buyer = User(
        fullname="Demo",
        email="email@email.com",
        password="password"
    )

    seller = User(
        fullname="Seller",
        email="seller@email.com",
        password="password"
    )

    buyer2 = User(
        fullname="Mike Miller",
        email="buyer@email.com",
        password="password"
    )

    db.session.add_all([buyer, seller])
    db.session.commit()

    # https://www.amazon.com/Philips-Sonicare-Toothbrush-Rechargeable-HX3681/dp/B09LD7WRVS

    product = Product(
        seller=seller,
        title="Philips Sonicare 4100 Power Toothbrush, Rechargeable Electric Toothbrush with Pressure Sensor, Black HX3681/24",
        price=39.99,
        description="Removes up to 5x more plaque vs. a manual toothbrush\nPressure sensor and two intensity settings protect sensitive gums from overbrushing\n2 minute SmarTimer with QuadPacer ensure Dentist-recommended brushing time\nBrush head replacement reminder ensures your brush head is always effective\nLong battery life with battery light indicator: One charge last for 2 weeks\nIncludes: 1 Philips Sonicare 4100 handle, 1 Optimal Plaque Control (C2) brush head, and 1 USB charger (wall adaptor not included)\nSRG, Test Report, CIPS918151 (2021)"
    )

    review = Review(
        product=product,
        buyer=buyer,
        rating=5,
        title="Amazing! Removes coffee / tea stains and plaque!",
        review="I generally write reviews when products seriously impress me or leave me very disappointed. This Philips Sonicare electric toothbrush did not disappoint. I have always been an analogue tooth brush user, but after this I have been converted.\nSome background: this year I started a new health regime and as part of that started drinking *lots* of coffee and tea. However several months in I noticed my teeth started to develop serious staining! This was despite brushing teeth very thoroughly twice a day. Regular brushing did not seem to help with my staining, and as time went by it continued to get worse and worse. I learned that plaque also stains more easily than enamel, and so this served to highlight all of the plaque in my mouth that had been accumulating over time.\nI did not want to reduce my coffee and tea consumption, nor did I want to go through abrasive teeth whitening procedures (also that would not solve my apparent plaque issue). After some research, I thought perhaps an electric toothbrush would help, so I bought this Sonicare and have not looked back. I brush twice a day, once in the morning and once at night. I do two cycles per brushing, one according to the instructions that come with the toothbrush, and another immediately after to focus on the more stained regions of my teeth.\nFast forward two months, and the stains on my front teeth have almost entirely disappeared! The plaque that had accumulated has also started to go away. I am seriously impressed, and never imagined that an electric toothbrush would have such a profound impact on my dental health! While it may be gross, see my attached photo. The light stain on the front left tooth used to cover over 80% of the surface. Now it is almost gone. My other teeth definitely need some tough love and care, but it is a major step in the right direction. It definitely takes time for the plaque to go away (do not expect magical results overnight), but with patience and proper brushing your oral health will certainly be improved.\nAside from the potent cleaning power of this toothbrush, the battery life is excellent, typically lasts me 3-4 weeks before alerting me to a recharge. Additionally it is rather portable, especially when you remove the toothbrush head from the body.\nIf you are not using an electric toothbrush, I urge you to make the swap. Your teeth will be so much cleaner. I can't say how my Sonic stacks up against other electric toothbrush brands, but I can say that this model certainly does the job."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/713c7c3UWrL._AC_UL320_.jpg"),
            preview=True
        ),
        ReviewImage(
            review=review,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/51H8iZ1vgwL._SY88.jpg"),
        ),
    ])

    # https://www.amazon.com/Oral-B-Black-Pro-1000-Rechargeable/dp/B01AKGRTUM
    product = Product(
        seller=seller,
        title="Oral-B Pro 1000 CrossAction Electric Toothbrush, Black",
        price=39.97,
        description="Clinically proven superior 3D cleaning oscillates and pulsates to break up and remove up to 300 percentage more plaque along the gum line than a regular manual toothbrush\nThe pressure sensor stops the pulsation movement if you brush too hard and the in handle timer helps you brush for a dentist recommended 2 minutes\n1 Mode, Daily Clean, rotates to break up and sweep away plaque\nIncluded in pack: 1 Oral B Professional Handle, 1 CrossAction Brush head and 1 charger\nCompatible with the following replacement toothbrush heads: CrossAction, 3D White, Sensitive Clean, Precision Clean, FlossAction, Deep Sweep, Ortho and Dual Clean. Does not fit iO brush heads\nPackaging may vary, Refill color may vary"
    )

    review = Review(
        product=product,
        buyer=buyer,
        rating=3,
        title="Get the Pro 1500 instead.",
        review="Update #2: I know the Pro 1500 isn't on Oral-B's website. When I bought the Pro 1500 nearly a year ago, I asked Oral-B why it's not on their site because I was concerned I had just bought a discontinued product. They assured me that it was in fact a brand new item that they had just released and that they were going to add the Pro 1500 to their site \"soon\".\n\nI realize that it's nearly a year later and they still haven't done it even though they are still manufacturing it, but I have been to their site several times per month since then and I can tell you that I'm honestly not surprised it's not on their site yet. I get the impression that anyone could do a better job with their site up-keep than whoever is doing it now. I have even noticed that it's kinda somewhat falling apart. Some elements no longer work and haven't worked for months. Their products are fine, they just need better people to handle and operate their website.\n\nUpdate #1: When I wrote this review, the price was the same for the Pro 1000 and Pro 1500 (including both the black and white Pro 1000s). Today, the price for the Pro 1500 nearly $20 more than it was when I wrote this review, and currently close to $30 more than the Pro 1000.\n\n[Original review below]\nI bought this to replace a very new Vitality. It was a *HUGE* upgrade over the Vitality, but then I saw the Pro 1500 and learned from Oral-B that it's quite superior. The Pro 1000's specs are:\n\n- 1 cleaning mode: Daily Clean\n- 8,800 oscillations per minute and 20,000 pulsations per minute on the Daily Clean mode\n- A pressure sensor that's supposed to just stop the pulsations when it's triggered\n- A pro timer that hesitates the motor once every 30 seconds, and 3 times every 2 minutes\n- A NiMH battery (old technology)\n- A battery life of 28 minutes (7 days, 2 minutes per day 2 times per day)\n- A full recharge time of 22 hours\n- A green charge indicator LED that blinks while charging, but stays off when it's not charging\n- A red battery level indicator that blinks a few times upon on/off if the battery needs to be charged\n- The CrossAction brush head\n\nThe Pro 1500's specs are:\n\n- 2 cleaning modes: Daily Clean and Sensitive\n- 9,900 oscillations per minute and 45,000 pulsations per minute on the Daily Clean mode (these speeds are faster than any I've seen so far in the specs of any of Oral-B's electric toothbrushes, including the Genius 8000 - they all seem to top out at 8,800 oscillations per minute and 40,000 pulsations per minute)\n- 7,400 oscillations per minute and 33,000 pulsations per minute on the Sensitive mode\n- A pressure sensor using a red LED that turns on when the pressure sensor is triggered\n- A pro timer that hesitates the motor once every 30 seconds, and 3 times every 2 minutes\n- A Lithium Ion battery\n- A battery life of 56 minutes (14 days, 2 minutes per day 2 times per day)\n- A full recharge time of 12 hours\n- A green charge indicator LED that blinks while charging, but stays off when it's not charging\n- A red battery level indicator that blinks a few times upon on/off if the battery needs to be charged.\n- The CrossAction brush head\n\nThe Vitality is extremely basic:\n\n- 1 cleaning mode: Daily Clean\n- 7,600 oscillations per minute.\n- A timer that hesitates the motor 3 times every 2 minutes\n- A NiMH battery\n- A battery life of 20 minutes (5 days, 2 minutes per day 2 times per day)\n- A full recharge time of 19 hours\n- No charge indicators or battery life indicators\n- Mine came with the Sensitive Gum Care brush head\n\nIn comparison, the Vitality seems like a cheap generic electric toothbrush. Don't consider buying it.\n\nWhen I upgraded to the Pro 1000, it was amazing. I wanted to burst at the seams and write an extremely rave review, but then I learned about *and ordered* the Oral-B Pro 1500. After using it, I can tell you that the Pro 1500 is *FAR* better than the Pro 1000. I honestly feel the Pro 1000 should be discontinued and no one should ever buy it. I mean really, the Pro 1500 is only $10 more right now and it destroys the Pro 1000.\n\nI would have given the Pro 1000 4 stars instead of just 3 if it had a Lithium Ion battery. They charge faster and last longer without charging.\n\nSo yeah, I am not sure I would recommend the Pro 1000 if you can get the Pro 1500. The Pro 1500 is a much wiser purchase. I'm *extremely* happy with mine. It blows the Pro 1000 out of the water."
    )

    review2 = Review(
        product=product,
        buyer=buyer2,
        rating=5,
        title="Basic but powerful.",
        review="I've used Oral-B electric toothbrushes for a long time. The battery lasts about a year and a half, so I replace the entire unit. Previous and more expensive models have a rubber comfort sleeve on the body, and I will say this comes loose after using and rinsing this brush 3 times a day. Water and paste will get trapped under. Gross.\n\nThis brush has a sleek plastic body, which solves this. It can get a bit slippery if wet, though.\n\nThe brush is as powerful as the higher priced brushes, which makes this a no brainer for me. Do I really need Bluetooth for my toothbrush??? lol."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/51rG8juGtnL._AC_UL320_.jpg"),
            preview=True
        ),
        review, review2
    ])

    # https://www.amazon.com/AquaSonic-Black-Ultra-Whitening-Toothbrush/dp/B072YVWBXH
    product = Product(
        seller=seller,
        title="Aquasonic Black Series Ultra Whitening Toothbrush – ADA Accepted Power Toothbrush - 8 Brush Heads & Travel Case – 40,000 VPM Electric Motor & Wireless Charging - 4 Modes w Smart Timer",
        price=39.95,
        description="40,000 VPM Smart Toothbrush – Beauty, brains and power. The Black Series is a world class modern electric toothbrush packed with the most up to date technology. It features an ultra-powerful and industry leading motor producing 40,000 vibrations per minute, a lithium-ion battery, ultra-fast wireless charging, 4 mode operation, smart vibration timers, 8 DuPont engineered brush heads, and a custom travel case; all with a sleek ultra-slim, lightweight and IPX7 rated waterproof design.\nAccepted by the American Dental Association (ADA) Council on Scientific Affairs – We put our money where your mouth is. Investing in premium oral care technologies has earned the Black Series the prestigious ADA seal of approval. It has shown efficacy in removing plaque and helping to prevent and reduce gingivitis. Black Series goes beyond just cleaning teeth – it provides complete oral care with unique modes that include one for whitening and polishing teeth, and one for improving gum health.\nModern Tech for a Healthy Smile - Black Series brings toothbrushes into modern times with its built-in enhanced features. A lithium-ion battery, ultra-fast wireless charging (forget outdated USB charging), 4 distinct brushing modes and a smart vibrating notification timer are some of the enhanced features built into the sleek and ergonomic waterproof black satin handle.\n8 DuPont Brush Heads & Travel Case Included – Included are 8 brush heads engineered by world famous DuPont; a world leader in quality & materials science. Each brush head lasts 3-4 months so 8 will last for about 2.5 years. Also included is a convenient custom hard shell travel case made of BPA-free plastic with space for two brush heads. Black Series can last 4 full weeks (2 min/2x a day) on a full charge so it's perfect for on the go travel with the included travel case.\nWhat's in the Box - 1 AquaSonic Black Series Smart Toothbrush, 1 wireless charging base, 8 DuPont brush heads, 1 travel case, warranty card, and user manual."
    )

    review = Review(
        product=product,
        buyer=buyer,
        rating=5,
        title="5 month update",
        review="bought june 2022 mow early dec\nusage is about 1 to 2x a day as i have oral b 1000 costco item\nbattery at gentle speeds with 1 to 3 full 2 minute sessions at a time each day will last TWO (2) months!!!!!!\ntake that you over priced oral b! which barely lastrs 7 days with 2x sessions each at 2 min.\n\nthe aquasonic will clean well\nstill find oral b simpler as i dont have to actually \"brush\" with OB as it does all the work for me\nbut AqS works at what i does and does better with rear molars esp the space between back two molars on each end of mouth (as in the lat two moalrs on each side of jaws)\n\ndownside? again wish it had slipperly reg plastic body w/o the soft touch coating. those eventually over time will degrade n become nasty sticky icky mess but...maybe thiers will notdos. if it does then ill just use adhesive remover\n\nthe oral b had 50 percent faiure rate as i bought 2pack from costco after 1 year, one failed to charge\nso time will tell if AaS is more durable and long lasting. i really hope so as it is is cuh a g8 value\n\n8 brush heads from ob? 60usd.\nfrom AqS? incld wih $40 toothbrush! that is 2 years of brush heads included!\n\noh i guess this is a downside but also could be how this thing lasts so long on a charge - you n need to charge 24 hours to get full 100% charge\n\nbut at same weight and zie as ob, not sure what kinda battery it uses but clearly far far far far superior to oral b\n\nthanks AqS!\n\nSorry for my typos! lol\n\nbottom line: buy this toothbrush\n\nAUg 31 2022 update\napprox usage 1-3 full cycles (2 min each cycle) daily\nstill havent had to charege the battery!!!!\non weekends, sometimes i have used it 3x a day with 1 - 2 ful lcycles\nmy oral b battery? horrible. lasts barealy a week without charging using 2x a day 1 cycle per usage. i keep it on charger most days\n\ncomparison:\nAS:\nsofter bristles\nlittle harder to get fully clean teet IMO as still havent gotten used to how to use it properly\namazing battery life - the review that said husband/wife use just one AS while switching brush tips, and it lasting for months, is not a lie. it is true i tell. true lol. i know cuz mine i have only done ONE 1x full 24 hour (which manual directs you to do - 24 hour for full charge). ive done that 1x back when i bought it.\nno weakening of power and its now aug 31th!\nsame size as Oral B housing yet AqZSn battery is clearly much bigger and of much higher quality than Oral B\nPrice for Aq includes 8 brush heads!\ni dont know if Azmn sells AqSn brush heads but i wont have to do so for a long time. 8 w each lasting 3 months would be 2 years worth of brush heads! and the price included the toothbrush!\nso while i do prefer easier brushing with OB, the AS is clearly a far better value and far better battery quality\nas one reviewer mentioned the AqSn brucsh head breaking, i am ultra gentle with my brushing to prevent that from occuring (i hope). tehoretically, same issue could occur with any of these electric toothbrushes\n\nCons:\nno power level indicator like OB has 3 leds for pwr. i wish AqS had this but as i said, im still on original charge 2 moths of usage !!! so the con is nitpicking lol\nstill havent really firgured out if i am brushing properly but i have same issue with a manual toothbrush lol\nbottom line:\nthe AS is superior to a reg toothbrush (by how much i dont know). i use level 2 power (not the max) and it seems to work well even with my feather light brushing of teeth\nwaterproof esseentially - iave rinsed entire housing repeatedly just like with my Oral B, neither has had issues\n\nthe one future con i foresee:\nthe brush head has a matte finish and all matte finshess become disgusting stickiy over time. i basiclaly will need to remove the matte finish at some point using heavy duty adhesive remover but that is oky.\n\nthe oral b does not have a matte finish which is batter.\n\nOral B\npoor battery life\nEXPENSIVE brush heads 55 for 9!\nexpensive to replace when battery eventually dies at 50 usd\nfloss action - these are the specific heads i use and they work great cuz they cover whole tooth\neasier to use than AquaS. as i simply hold over each tooth and let OB do the work\nSTIFF bristiles though\noverall OB cleans better IMO\n\nJune 26 2022\nonly used 1x just initial impressions will update later\n\nive used oralb 3d series from costco for 2 years using their floss action head\npros of OB is effortless - all ii have to do is hold the brush feather lightly agasinst teeth vertically - not movement needed like standard toothbrush\n\nAquasonic Sonic Toothbrush has an accurate title which means it is a toothbrush with a sonic function.\ni have no idea if this sonic function 40k bpm actually does anything....\ni was hoping for a $30 oral-b replacement but instead it is a standard toothbrush with a sonic funciton meaning i stilll have to brush my teeth like a normal toothbrush.\n\nwhine whine whin i konw ha ha ha\nbut i have i bone spurs in shoulders blades where upper movent causes pain hence my preference for oral b no effort tootbrushing over aquasonic.\n\ni will stil keep and use aquasonic as as a backup to my oral b\n\nwill update later once ive used long term\n\nbut again, best value for money for a toothbrush with sonic function...but again...does it actually remove plque better than standard ultra soft tootbrush???? i konw ora-b floss action head does work better but does aquasonic????\n\ntime will tel.... will update later and sorry for typos"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/716hFx-iA3L._AC_UL320_.jpg"),
            preview=True
        ),
        review
    ])

    product = Product(
        seller=seller,
        title="Philips Sonicare 4100 Power Toothbrush, Rechargeable Electric Toothbrush with Pressure Sensor, Black HX3681/24",
        price=39.99,
        description="Removes up to 5x more plaque vs. a manual toothbrush\nPressure sensor and two intensity settings protect sensitive gums from overbrushing\n2 minute SmarTimer with QuadPacer ensure Dentist-recommended brushing time\nBrush head replacement reminder ensures your brush head is always effective\nLong battery life with battery light indicator: One charge last for 2 weeks\nIncludes: 1 Philips Sonicare 4100 handle, 1 Optimal Plaque Control (C2) brush head, and 1 USB charger (wall adaptor not included)\nSRG, Test Report, CIPS918151 (2021)"
    )

    review = Review(
        product=product,
        buyer=buyer,
        rating=5,
        review="I generally write reviews when products seriously impress me or leave me very disappointed. This Philips Sonicare electric toothbrush did not disappoint. I have always been an analogue tooth brush user, but after this I have been converted.\nSome background: this year I started a new health regime and as part of that started drinking *lots* of coffee and tea. However several months in I noticed my teeth started to develop serious staining! This was despite brushing teeth very thoroughly twice a day. Regular brushing did not seem to help with my staining, and as time went by it continued to get worse and worse. I learned that plaque also stains more easily than enamel, and so this served to highlight all of the plaque in my mouth that had been accumulating over time.\nI did not want to reduce my coffee and tea consumption, nor did I want to go through abrasive teeth whitening procedures (also that would not solve my apparent plaque issue). After some research, I thought perhaps an electric toothbrush would help, so I bought this Sonicare and have not looked back. I brush twice a day, once in the morning and once at night. I do two cycles per brushing, one according to the instructions that come with the toothbrush, and another immediately after to focus on the more stained regions of my teeth.\nFast forward two months, and the stains on my front teeth have almost entirely disappeared! The plaque that had accumulated has also started to go away. I am seriously impressed, and never imagined that an electric toothbrush would have such a profound impact on my dental health! While it may be gross, see my attached photo. The light stain on the front left tooth used to cover over 80% of the surface. Now it is almost gone. My other teeth definitely need some tough love and care, but it is a major step in the right direction. It definitely takes time for the plaque to go away (do not expect magical results overnight), but with patience and proper brushing your oral health will certainly be improved.\nAside from the potent cleaning power of this toothbrush, the battery life is excellent, typically lasts me 3-4 weeks before alerting me to a recharge. Additionally it is rather portable, especially when you remove the toothbrush head from the body.\nIf you are not using an electric toothbrush, I urge you to make the swap. Your teeth will be so much cleaner. I can't say how my Sonic stacks up against other electric toothbrush brands, but I can say that this model certainly does the job."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/713c7c3UWrL._AC_UL320_.jpg"),
            preview=True
        ),
        ReviewImage(
            review=review,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/51H8iZ1vgwL._SY88.jpg"),
        ),
    ])

    product = Product(
        seller=seller,
        title="Philips Sonicare 4100 Power Toothbrush, Rechargeable Electric Toothbrush with Pressure Sensor, Black HX3681/24",
        price=39.99,
        description="Removes up to 5x more plaque vs. a manual toothbrush\nPressure sensor and two intensity settings protect sensitive gums from overbrushing\n2 minute SmarTimer with QuadPacer ensure Dentist-recommended brushing time\nBrush head replacement reminder ensures your brush head is always effective\nLong battery life with battery light indicator: One charge last for 2 weeks\nIncludes: 1 Philips Sonicare 4100 handle, 1 Optimal Plaque Control (C2) brush head, and 1 USB charger (wall adaptor not included)\nSRG, Test Report, CIPS918151 (2021)"
    )

    review = Review(
        product=product,
        buyer=buyer,
        rating=5,
        review="I generally write reviews when products seriously impress me or leave me very disappointed. This Philips Sonicare electric toothbrush did not disappoint. I have always been an analogue tooth brush user, but after this I have been converted.\nSome background: this year I started a new health regime and as part of that started drinking *lots* of coffee and tea. However several months in I noticed my teeth started to develop serious staining! This was despite brushing teeth very thoroughly twice a day. Regular brushing did not seem to help with my staining, and as time went by it continued to get worse and worse. I learned that plaque also stains more easily than enamel, and so this served to highlight all of the plaque in my mouth that had been accumulating over time.\nI did not want to reduce my coffee and tea consumption, nor did I want to go through abrasive teeth whitening procedures (also that would not solve my apparent plaque issue). After some research, I thought perhaps an electric toothbrush would help, so I bought this Sonicare and have not looked back. I brush twice a day, once in the morning and once at night. I do two cycles per brushing, one according to the instructions that come with the toothbrush, and another immediately after to focus on the more stained regions of my teeth.\nFast forward two months, and the stains on my front teeth have almost entirely disappeared! The plaque that had accumulated has also started to go away. I am seriously impressed, and never imagined that an electric toothbrush would have such a profound impact on my dental health! While it may be gross, see my attached photo. The light stain on the front left tooth used to cover over 80% of the surface. Now it is almost gone. My other teeth definitely need some tough love and care, but it is a major step in the right direction. It definitely takes time for the plaque to go away (do not expect magical results overnight), but with patience and proper brushing your oral health will certainly be improved.\nAside from the potent cleaning power of this toothbrush, the battery life is excellent, typically lasts me 3-4 weeks before alerting me to a recharge. Additionally it is rather portable, especially when you remove the toothbrush head from the body.\nIf you are not using an electric toothbrush, I urge you to make the swap. Your teeth will be so much cleaner. I can't say how my Sonic stacks up against other electric toothbrush brands, but I can say that this model certainly does the job."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/713c7c3UWrL._AC_UL320_.jpg"),
            preview=True
        ),
        ReviewImage(
            review=review,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/51H8iZ1vgwL._SY88.jpg"),
        ),
    ])

    product = Product(
        seller=seller,
        title="Philips Sonicare 4100 Power Toothbrush, Rechargeable Electric Toothbrush with Pressure Sensor, Black HX3681/24",
        price=39.99,
        description="Removes up to 5x more plaque vs. a manual toothbrush\nPressure sensor and two intensity settings protect sensitive gums from overbrushing\n2 minute SmarTimer with QuadPacer ensure Dentist-recommended brushing time\nBrush head replacement reminder ensures your brush head is always effective\nLong battery life with battery light indicator: One charge last for 2 weeks\nIncludes: 1 Philips Sonicare 4100 handle, 1 Optimal Plaque Control (C2) brush head, and 1 USB charger (wall adaptor not included)\nSRG, Test Report, CIPS918151 (2021)"
    )

    review = Review(
        product=product,
        buyer=buyer,
        rating=5,
        review="I generally write reviews when products seriously impress me or leave me very disappointed. This Philips Sonicare electric toothbrush did not disappoint. I have always been an analogue tooth brush user, but after this I have been converted.\nSome background: this year I started a new health regime and as part of that started drinking *lots* of coffee and tea. However several months in I noticed my teeth started to develop serious staining! This was despite brushing teeth very thoroughly twice a day. Regular brushing did not seem to help with my staining, and as time went by it continued to get worse and worse. I learned that plaque also stains more easily than enamel, and so this served to highlight all of the plaque in my mouth that had been accumulating over time.\nI did not want to reduce my coffee and tea consumption, nor did I want to go through abrasive teeth whitening procedures (also that would not solve my apparent plaque issue). After some research, I thought perhaps an electric toothbrush would help, so I bought this Sonicare and have not looked back. I brush twice a day, once in the morning and once at night. I do two cycles per brushing, one according to the instructions that come with the toothbrush, and another immediately after to focus on the more stained regions of my teeth.\nFast forward two months, and the stains on my front teeth have almost entirely disappeared! The plaque that had accumulated has also started to go away. I am seriously impressed, and never imagined that an electric toothbrush would have such a profound impact on my dental health! While it may be gross, see my attached photo. The light stain on the front left tooth used to cover over 80% of the surface. Now it is almost gone. My other teeth definitely need some tough love and care, but it is a major step in the right direction. It definitely takes time for the plaque to go away (do not expect magical results overnight), but with patience and proper brushing your oral health will certainly be improved.\nAside from the potent cleaning power of this toothbrush, the battery life is excellent, typically lasts me 3-4 weeks before alerting me to a recharge. Additionally it is rather portable, especially when you remove the toothbrush head from the body.\nIf you are not using an electric toothbrush, I urge you to make the swap. Your teeth will be so much cleaner. I can't say how my Sonic stacks up against other electric toothbrush brands, but I can say that this model certainly does the job."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/713c7c3UWrL._AC_UL320_.jpg"),
            preview=True
        ),
        ReviewImage(
            review=review,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/51H8iZ1vgwL._SY88.jpg"),
        ),
    ])

    product = Product(
        seller=seller,
        title="Philips Sonicare 4100 Power Toothbrush, Rechargeable Electric Toothbrush with Pressure Sensor, Black HX3681/24",
        price=39.99,
        description="Removes up to 5x more plaque vs. a manual toothbrush\nPressure sensor and two intensity settings protect sensitive gums from overbrushing\n2 minute SmarTimer with QuadPacer ensure Dentist-recommended brushing time\nBrush head replacement reminder ensures your brush head is always effective\nLong battery life with battery light indicator: One charge last for 2 weeks\nIncludes: 1 Philips Sonicare 4100 handle, 1 Optimal Plaque Control (C2) brush head, and 1 USB charger (wall adaptor not included)\nSRG, Test Report, CIPS918151 (2021)"
    )

    review = Review(
        product=product,
        buyer=buyer,
        rating=5,
        review="I generally write reviews when products seriously impress me or leave me very disappointed. This Philips Sonicare electric toothbrush did not disappoint. I have always been an analogue tooth brush user, but after this I have been converted.\nSome background: this year I started a new health regime and as part of that started drinking *lots* of coffee and tea. However several months in I noticed my teeth started to develop serious staining! This was despite brushing teeth very thoroughly twice a day. Regular brushing did not seem to help with my staining, and as time went by it continued to get worse and worse. I learned that plaque also stains more easily than enamel, and so this served to highlight all of the plaque in my mouth that had been accumulating over time.\nI did not want to reduce my coffee and tea consumption, nor did I want to go through abrasive teeth whitening procedures (also that would not solve my apparent plaque issue). After some research, I thought perhaps an electric toothbrush would help, so I bought this Sonicare and have not looked back. I brush twice a day, once in the morning and once at night. I do two cycles per brushing, one according to the instructions that come with the toothbrush, and another immediately after to focus on the more stained regions of my teeth.\nFast forward two months, and the stains on my front teeth have almost entirely disappeared! The plaque that had accumulated has also started to go away. I am seriously impressed, and never imagined that an electric toothbrush would have such a profound impact on my dental health! While it may be gross, see my attached photo. The light stain on the front left tooth used to cover over 80% of the surface. Now it is almost gone. My other teeth definitely need some tough love and care, but it is a major step in the right direction. It definitely takes time for the plaque to go away (do not expect magical results overnight), but with patience and proper brushing your oral health will certainly be improved.\nAside from the potent cleaning power of this toothbrush, the battery life is excellent, typically lasts me 3-4 weeks before alerting me to a recharge. Additionally it is rather portable, especially when you remove the toothbrush head from the body.\nIf you are not using an electric toothbrush, I urge you to make the swap. Your teeth will be so much cleaner. I can't say how my Sonic stacks up against other electric toothbrush brands, but I can say that this model certainly does the job."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/713c7c3UWrL._AC_UL320_.jpg"),
            preview=True
        ),
        ReviewImage(
            review=review,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/51H8iZ1vgwL._SY88.jpg"),
        ),
    ])

    product = Product(
        seller=seller,
        title="Philips Sonicare 4100 Power Toothbrush, Rechargeable Electric Toothbrush with Pressure Sensor, Black HX3681/24",
        price=39.99,
        description="Removes up to 5x more plaque vs. a manual toothbrush\nPressure sensor and two intensity settings protect sensitive gums from overbrushing\n2 minute SmarTimer with QuadPacer ensure Dentist-recommended brushing time\nBrush head replacement reminder ensures your brush head is always effective\nLong battery life with battery light indicator: One charge last for 2 weeks\nIncludes: 1 Philips Sonicare 4100 handle, 1 Optimal Plaque Control (C2) brush head, and 1 USB charger (wall adaptor not included)\nSRG, Test Report, CIPS918151 (2021)"
    )

    review = Review(
        product=product,
        buyer=buyer,
        rating=5,
        review="I generally write reviews when products seriously impress me or leave me very disappointed. This Philips Sonicare electric toothbrush did not disappoint. I have always been an analogue tooth brush user, but after this I have been converted.\nSome background: this year I started a new health regime and as part of that started drinking *lots* of coffee and tea. However several months in I noticed my teeth started to develop serious staining! This was despite brushing teeth very thoroughly twice a day. Regular brushing did not seem to help with my staining, and as time went by it continued to get worse and worse. I learned that plaque also stains more easily than enamel, and so this served to highlight all of the plaque in my mouth that had been accumulating over time.\nI did not want to reduce my coffee and tea consumption, nor did I want to go through abrasive teeth whitening procedures (also that would not solve my apparent plaque issue). After some research, I thought perhaps an electric toothbrush would help, so I bought this Sonicare and have not looked back. I brush twice a day, once in the morning and once at night. I do two cycles per brushing, one according to the instructions that come with the toothbrush, and another immediately after to focus on the more stained regions of my teeth.\nFast forward two months, and the stains on my front teeth have almost entirely disappeared! The plaque that had accumulated has also started to go away. I am seriously impressed, and never imagined that an electric toothbrush would have such a profound impact on my dental health! While it may be gross, see my attached photo. The light stain on the front left tooth used to cover over 80% of the surface. Now it is almost gone. My other teeth definitely need some tough love and care, but it is a major step in the right direction. It definitely takes time for the plaque to go away (do not expect magical results overnight), but with patience and proper brushing your oral health will certainly be improved.\nAside from the potent cleaning power of this toothbrush, the battery life is excellent, typically lasts me 3-4 weeks before alerting me to a recharge. Additionally it is rather portable, especially when you remove the toothbrush head from the body.\nIf you are not using an electric toothbrush, I urge you to make the swap. Your teeth will be so much cleaner. I can't say how my Sonic stacks up against other electric toothbrush brands, but I can say that this model certainly does the job."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/713c7c3UWrL._AC_UL320_.jpg"),
            preview=True
        ),
        ReviewImage(
            review=review,
            url=upload_image_to_bucket_from_url(
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/51H8iZ1vgwL._SY88.jpg"),
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
