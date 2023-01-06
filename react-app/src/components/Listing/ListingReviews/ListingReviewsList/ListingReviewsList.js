// import Stars from "../../../Stars/Stars";
import styles from "./ListingReviewsList.module.css"

export default function ListingReviewsList({ product, reviews }) {
    if (reviews.length === 0 || reviews[0].product_id !== product.id) return;

    return (
        <div className={styles.wrapper}>
            {reviews.map((review, i) => <div key={i}>{review.review}</div>)}
        </div>
    );
}
