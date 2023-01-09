import styles from "./ListingReviewsBreakdown.module.css"

import StarsBig from "../../../StarsBig/StarsBig"
import RatingBar from "./RatingBar/RatingBar";

export default function ListingReviewsBreakdown({ product, reviews }) {
    const percents = reviews.reduce((counts, review) => {
        counts[review.rating]++;
        return counts;
    }, { 5: 0, 4: 0, 3: 0, 2: 0, 1: 0 });
    percents["5"] = percents["5"] / reviews.length * 100;
    percents["4"] = percents["4"] / reviews.length * 100;
    percents["3"] = percents["3"] / reviews.length * 100;
    percents["2"] = percents["2"] / reviews.length * 100;
    percents["1"] = percents["1"] / reviews.length * 100;

    return (
        <div className={styles.wrapper}>
            <div className={styles.heading}>Customer reviews</div>
            {product.num_ratings > 0 && <div className={styles.summary}><StarsBig rating={product.avg_rating} /> <span className={styles.summaryText}>{parseFloat(product.avg_rating).toFixed(1)} out of 5</span></div>}
            <div className={styles.count}>{product.num_ratings} global rating{product.num_ratings === 1 ? "" : "s"}</div>
            <RatingBar percents={percents} rating={5} />
            <RatingBar percents={percents} rating={4} />
            <RatingBar percents={percents} rating={3} />
            <RatingBar percents={percents} rating={2} />
            <RatingBar percents={percents} rating={1} />
        </div>
    );
}
