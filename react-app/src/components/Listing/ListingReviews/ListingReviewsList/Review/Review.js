import styles from "./Review.module.css"

import Stars from "../../../../Stars/Stars";

export default function Review({ review }) {
    let reviewDate = new Date(review.created_at);
    reviewDate = reviewDate.toLocaleDateString('en-us', { year: "numeric", month: "long", day: "numeric" });

    return (
        <div className={styles.wrapper}>

            <div className={styles.profile}>
                <img className={styles.profileImage} src="/images/profile.jpg" alt="profile" />
                <div className={styles.name}>{review.buyer.fullname}</div>
            </div>

            <div className={styles.rating}>
                <Stars rating={review.rating} />
                <div className={styles.title}>{review.title}</div>
            </div>

            <div className={styles.date}>
                Reviewed in the United States 🇺🇸 on {reviewDate}
            </div>

            <div className={styles.review}>{review.review}</div>
        </div>
    );
}
