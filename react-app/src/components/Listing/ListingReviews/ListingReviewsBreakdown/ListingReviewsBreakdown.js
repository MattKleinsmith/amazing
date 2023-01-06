import styles from "./ListingReviewsBreakdown.module.css"

import StarsBig from "../../../StarsBig/StarsBig"

export default function ListingReviewsBreakdown({ product }) {

    return (
        <div className={styles.wrapper}>
            <div className={styles.heading}>Customer reviews</div>
            <StarsBig rating={product.avg_rating} />
        </div>
    );
}
