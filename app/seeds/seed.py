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

    # https://www.amazon.com/AquaSonic-Black-Ultra-Whitening-Toothbrush/dp/B072YVWBXH/ref=sr_1_7?crid=1MHRV85VL98TQ&keywords=electric+toothbrushes&qid=1673123471&s=hpc&sprefix=electric+toothbrushes%2Chpc%2C74&sr=1-7

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

        Review(
            buyer=brian,
            product=product,
            rating=5.0,
            review="bought june 2022 mow early dec\nusage is about 1 to 2x a day as i have oral b 1000 costco item\nbattery at gentle speeds with 1 to 3 full 2 minute sessions at a time each day will last TWO (2) months!!!!!!\ntake that you over priced oral b! which barely lastrs 7 days with 2x sessions each at 2 min.\n\nthe aquasonic will clean well\nstill find oral b simpler as i dont have to actually 'brush' with OB as it does all the work for me\nbut AqS works at what i does and does better with rear molars esp the space between back two molars on each end of mouth (as in the lat two moalrs on each side of jaws)\n\ndownside? again wish it had slipperly reg plastic body w/o the soft touch coating. those eventually over time will degrade n become nasty sticky icky mess but...maybe thiers will notdos. if it does then ill just use adhesive remover\n\nthe oral b had 50 percent faiure rate as i bought 2pack from costco after 1 year, one failed to charge\nso time will tell if AaS is more durable and long lasting. i really hope so as it is is cuh a g8 value\n\n8 brush heads from ob? 60usd.\nfrom AqS? incld wih $40 toothbrush! that is 2 years of brush heads included!\n\noh i guess this is a downside but also could be how this thing lasts so long on a charge - you n need to charge 24 hours to get full 100% charge\n\nbut at same weight and zie as ob, not sure what kinda battery it uses but clearly far far far far superior to oral b\n\nthanks AqS!\n\nSorry for my typos! lol\n\nbottom line: buy this toothbrush\n\nAUg 31 2022 update\napprox usage 1-3 full cycles (2 min each cycle) daily\nstill havent had to charege the battery!!!!\non weekends, sometimes i have used it 3x a day with 1 - 2 ful lcycles\nmy oral b battery? horrible. lasts barealy a week without charging using 2x a day 1 cycle per usage. i keep it on charger most days\n\ncomparison:\nAS:\nsofter bristles\nlittle harder to get fully clean teet IMO as still havent gotten used to how to use it properly\namazing battery life - the review that said husband/wife use just one AS while switching brush tips, and it lasting for months, is not a lie. it is true i tell. true lol. i know cuz mine i have only done ONE 1x full 24 hour (which manual directs you to do - 24 hour for full charge). ive done that 1x back when i bought it.\nno weakening of power and its now aug 31th!\nsame size as Oral B housing yet AqZSn battery is clearly much bigger and of much higher quality than Oral B\nPrice for Aq includes 8 brush heads!\ni dont know if Azmn sells AqSn brush heads but i wont have to do so for a long time. 8 w each lasting 3 months would be 2 years worth of brush heads! and the price included the toothbrush!\nso while i do prefer easier brushing with OB, the AS is clearly a far better value and far better battery quality\nas one reviewer mentioned the AqSn brucsh head breaking, i am ultra gentle with my brushing to prevent that from occuring (i hope). tehoretically, same issue could occur with any of these electric toothbrushes\n\nCons:\nno power level indicator like OB has 3 leds for pwr. i wish AqS had this but as i said, im still on original charge 2 moths of usage !!! so the con is nitpicking lol\nstill havent really firgured out if i am brushing properly  but i have same issue with a manual toothbrush lol\nbottom line:\nthe AS is superior to a reg toothbrush (by how much i dont know). i use level 2 power (not the max) and it seems to work well even with my feather light brushing of teeth\nwaterproof esseentially - iave rinsed entire housing repeatedly just like with my Oral B, neither has had issues\n\nthe one future con i foresee:\nthe brush head has a matte finish and all matte finshess become disgusting stickiy over time. i basiclaly will need to remove the matte finish at some point using heavy duty  adhesive remover but that is oky.\n\nthe oral b does not have a matte finish which is batter.\n\nOral B\npoor battery life\nEXPENSIVE brush heads 55 for 9!\nexpensive to replace when battery eventually dies at 50 usd\nfloss action - these are the specific heads i use and they work great cuz they cover whole tooth\neasier to use than AquaS. as i simply hold over each tooth and let OB do the work\nSTIFF bristiles though\noverall OB cleans better IMO\n\nJune 26 2022\nonly used 1x just initial impressions will update later\n\nive used oralb 3d series from costco for 2 years using their floss action head\npros of OB is effortless - all ii have to do is hold the brush feather lightly agasinst teeth vertically - not movement needed like standard toothbrush\n\nAquasonic Sonic Toothbrush has an accurate title which means it is a toothbrush with a sonic function.\ni have no idea if this sonic function 40k bpm actually does anything....\ni was hoping for a $30 oral-b replacement but instead it is a standard toothbrush with a sonic funciton meaning i stilll have to brush my teeth like a normal toothbrush.\n\nwhine whine whin i konw ha ha ha\nbut i have i bone spurs in shoulders blades where upper movent causes pain hence my preference for oral b no effort tootbrushing over aquasonic.\n\ni will stil keep and use aquasonic as as a backup to my oral b\n\nwill update later once ive used long term\n\nbut again, best value for money for a toothbrush with sonic function...but again...does it actually remove plque better than standard ultra soft tootbrush???? i konw ora-b floss action head does work better but does aquasonic????\n\ntime will tel.... will update later and sorry for typos",
            title="5 month update"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=2.0,
            review="The image included with this review is to provide a reference point for review. My previous e-brush is a sonicare g2 series (nowadays i found i can interchange the heads for different series, as the brush i have allows for most features present in other devices). the sonicare cost me around $50-60 (can't really remember) at the time of purchase (around four years ago, which speaks to sonicare's longevity). the brush still works well, i will add, just that i don't like the price point for replacing the brushhead, and nowadays i have noticed a slight reduction in speed and battery longevity (although mostly i just wanted to try something new after four years of the same brand).\n  i heard about this aquasonic with the significantly reduced brushhead pricepoint (i buy my heads at Costco at 2 for $18 before taxes, whereas aquasonic comes with 8 brushheads at $34.99 for the entire set, including brush and travelcase). Overall, I would say I am VERY impressed with the Aquasonic. I have tried Oral-B and other brands that have came and went throughout the years (i found that sonicare had softer brushes and the overall experience was better for me), so I have a decent general idea of what's out there. I have had the item for a weej and will try to update periodically as i know ebrushes are a significant investment for some (especially families) that are new to the experience, and it can be difficult to trust reviewers nowadays.\n  Here are Pros and Cons:\nPros\n  The smooth matte-like feel of the brush (which surprisingly no one talked about in the reviews i read), which immediately caught my attention. it makes me WANT to use the brush.\n  The lightweight feel of the brush in my hand. It is actually noticeably lighter than my sonicare, which i already loved for how lightweight it was.  For the price, this was one of the shockers.\n  The SOFTNESS of the brush itself. Some reviewers noticed the small size (this tells me they probably haven't had an ebrush before because some dentists online actually say a smaller size is ideal for greater teeth coverage), yet as you can tell it's about the same size as my sonicare (if not slightly bigger). I have senaitive teeth and my dentist keeps telling me the apfter the better. i legit didn't think there was an ebrush softer than my sonicare (the g2 series is designed specifically to be soft). again, for the price point, another shocker.\n  The mode selection text. This might seem obvious, yet most ebrushes i have used in the past only have a light that blinks and tells you the mode you're on in a more subtle way. i was indifferent to this feature as i want to believe i am smart enough to understand the blinking system and the vibration of the brush to understand which mode i am in, however, i have to admit it definitely makes it easier and to my taste does not remove any points in the aesthetics department.\n  the cleaning power. this also shocked me a bit because, again, for the price point this brush works as well if not better than my sonicare. there's also a noticeable difference between each mode, compelling me to believe that the other modes are just as effective in their intended purpose (i have only tried the massage and clean modes, and they do what they say they'll do).\n  the attachment process. the setup is the same as my sonicare (to the extent that i wouldn't be surprised if this company used the sonicare design as inspiration, because it is pretty similar\n in key areas yet surprisingly better overall, in my opinion, so far), with the head attaching to the base of the brush with a simple push and pull feature.\n  the two button difference for power on/off and mode. this definitely tells me they hsve learned from the user experience in other brushes because that has been one of my pet peeves— one button to select them all with only the blinker to guide you. the peeve is mostly with the time consumption (as some ebrushes require a hold in order to change modes or to change quadrant features). this brush also has quadrant features that seem more fluid than my sonicare.\n  i will also give points for aesthetics, as the entire setup looks well-thought out (as in, they probably just got the better features of other ebrushes and went with that 😂 ).\n  the travel case. the sonocare comes with brushhead cover, which i actually love for its simplicity and utility, yet the idea of a cover somehow feels more thoughtful (even though the head cover is actually more functional).\n Cons\n  i don't know yet (just a week in).\n  i will update as i go to podt any issues. i got the 3-year insurance due to how cheap it was and the fact that if this covers me for 3 years, it will automatically make it as long-lasting as my sonicare (even better, considering sonicare warranty only covered me for one year).\n  i will say this— i LOVE my sonicare and am in no way bashing. if you want a durable, quality brush, go with sonicare (i will vouch for them).  Phillips (the parent company of sonicare) is well known for their quality products, yet lately i have noticed better price points elsewhere. at some point the drop in price overwhelms the quality, as long as there is a base function that's being met. So far this aquasonic is merting that base function, and some. if this continue for as long as the warranty is covered, i definitely can say i am going with aquasonic in the future. i am also content with knowing i don't have to worry about a trip to the store for a replacement head for at least two years (i was starting to dread having to get new replacements for my sonicare with greater frequency, as i can almost say that the color indicator on the brush keeps getting shorter and shorter in lifespan lately). this will be my best reason to get the aquasonic, as i don't like it when a company uses Rockefeller tactics (we're in 2021, and those tactics were conceived of in the 1920s).\n###\n\n***UPDATE--- One Month After Purchase***\n  So, the previous review was not bad on the Aquasonic, yet after a while of only using this bruah I started to notice that there was starting to show some plaque build-up on my teeth. This was confusing because my Sonicare isually took care of any buildup quite easily, and most other legit ebrushes have a similar capacity. I started to think maybe I wasn't brushing 'right' yet that didn't make sense because I have been brushing about the same for either brush. Thankfully I didn't toss my Sonicare, because, as previously mentioned, it still worked just fine after four-five years of use.\n  Well, whay do you know? The Sonicare took care of the plaque with ease (which was a relief because after a while it is nearly impossible to remove plaque on teeth and I have to wait for biannual checkup to have a hygienist do it, which can be a bit embarrassing but that is what they do so whatever). Someone else on another review mentioned how Aquasonic was a bruah that just vibrated and did nothing. Well, now I know what they mean.\n  This brush is amazing for decorative purposes, yet is you want to save yourself a trip to the hygienist, get a quality, reputable brand. As with anything, you pay what you get. I especially appreciate the Sonicare took care of in-between teeth plaque as well (for those of you who don't know, you van 'feel' plaque on teeth when you feel something rough on the surface of teeth. Your teeth are naturally smooth and feels good when the tongue glides over a set of clean, plaque-free teeth. Also, there is a chemical agent provided by my hygienist for checking for plaque, which can be expensive and only meant to be used periodically and not even weekly.).\n  Well, that was a waste of $40+tax.\n  For thise whi might say, 'Well, you just have to brush harder or provide more motion', I say this— that is the whole point of an ebrush, that you don't have to do much and the brush does all the work for you. If I have to put in work, it's a manual brush (which I also have for travel/work and emergencies when I forget to pack my ebruah for travel, and there's nothing wrong with using a manual brush other than that in my experience a good ebrush will keep your teeth as plaque-free as possible). That defeats the whole point of buying an ebrush.\n  This Aquasonic looks great and feels great, yet it doesn't perform its stated function. That's like a beautiful car that doesn't drive, you have to push it yourself. It looks beautiful and aggressive, like it can go fast, yet ultimately it doesn't go anywhere. It doesn't perform its intended function (unless you're the kind of person that likes to spend money on decorative vehicles, which I am sure is a niche market rhat does exist). Please be advised of this, as it mifht save you a visit to a hygienist (you go to your dentist twice a year but sometimes even dentists don't have the specialist experience to clean and polish teeth like a hygienist, which sometimes requires special equipment that uses water, air, and baking soda at once.). I was abke to experiment and now am probably going to have to visit my hygienist anyway, but I was willing to take that risk. I understand not everyone has the cash to take that risk, so be warned.",
            title="Unexpectedly Great, Until It Isn't. Buy Reputable Quality Instead."
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
                "https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/7117K2Ej9AS._SY450_.jpg"),
            preview=True,
            position=1
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
