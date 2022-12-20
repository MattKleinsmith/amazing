import FiveStars from "../../../FiveStars/FiveStars";
import ListingReviewsItem from "./ListingReviewsItem/ListingReviewsItem";
import styles from "./ListingReviews.module.css";

export default function ListingReviews({ product }) {
    const reviews = []

    if (!reviews) return;
    return (
        <div className={styles.wrapper}>
            <div className={styles.reviewSummary}>
                <div className={styles.reviewNumber}>
                    {reviews.length} reviews
                </div>
                <div className={styles.reviewStars}>
                    <FiveStars style={{ fontSize: '1rem' }} rating={product.product_rating} />
                </div>
            </div>
            <div className={styles.ListingReviews}>
                {reviews.map((review, i) => <ListingReviewsItem key={i} review={review} />)}
            </div>
        </div>
    );
}
