// import Stars from "../../../../Stars/Stars";
import styles from "./Review.module.css"

export default function Review({ review }) {
    // let reviewDate = new Date(review.created_at);
    // reviewDate = reviewDate.toLocaleDateString('en-us', { weekday: "short", year: "numeric", month: "short", day: "numeric" });

    return (
        <div className={styles.wrapper}>
            <div className={styles.profile}>
                <img className={styles.profileImage} src="/images/profile.jpg" alt="profile" />
                <div className={styles.name}>{review.buyer.fullname}</div>
            </div>
        </div>
    );
}
