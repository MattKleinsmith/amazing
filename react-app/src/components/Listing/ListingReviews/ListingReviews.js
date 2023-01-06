import styles from "./ListingReviews.module.css";
import ListingReviewsBreakdown from "./ListingReviewsBreakdown/ListingReviewsBreakdown";
import ListingReviewsList from "./ListingReviewsList/ListingReviewsList";

export default function ListingReviews({ product }) {
    const reviews = []

    if (!reviews) return;
    return (
        <div className={styles.wrapper}>
            <ListingReviewsBreakdown product={product} />
            <ListingReviewsList product={product} />
        </div>
    );
}
