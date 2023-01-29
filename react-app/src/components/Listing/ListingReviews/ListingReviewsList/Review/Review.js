import styles from "./Review.module.css"

import Stars from "../../../../Stars/Stars";

export default function Review({ review }) {
    let reviewDate = new Date(review.created_at);
    reviewDate = reviewDate.toLocaleDateString('en-us', { year: "numeric", month: "long", day: "numeric" });

    return (
        <div className={styles.wrapper}>

            <div className={styles.profile}>
                <img className={styles.profileImage} src="https://d1irxr40exwge2.cloudfront.net/profile.jpg" alt="profile" />
                <div className={styles.name}>{review.buyer.fullname}</div>
            </div>

            <div className={styles.rating}>
                <div><Stars rating={review.rating} /></div>
                <div className={styles.title}>{review.title}</div>
            </div>

            <div className={styles.date}>
                Reviewed in the United States 🇺🇸 on {reviewDate}
            </div>

            <div className={styles.review}>{review.review}</div>

            <div className={styles.images}>
                {review.review_images.length > 0 && review.review_images.map((image, i) => <img className={styles.image} src={image.url} alt="review" key={i} />)}
            </div>
        </div>
    );
}
