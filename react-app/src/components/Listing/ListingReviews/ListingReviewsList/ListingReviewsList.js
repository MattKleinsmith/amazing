// import Stars from "../../../Stars/Stars";
import styles from "./ListingReviewsList.module.css"
import Review from "./Review/Review"

export default function ListingReviewsList({ product, reviews }) {
    if (reviews.length === 0 || reviews[0].product_id !== product.id) return;
    const images = reviews.filter(review => review.review_images.length > 0).map(review => review.review_images[0]).slice(0, 4);
    console.log("reviews", reviews);
    console.log("images", images);
    return (
        <div className={styles.wrapper}>
            <div>
                <div className={styles.heading}>Review images</div>
                <div>{images.map((image, i) => <img className={styles.image} key={i} alt={i} src={image.url} />)}</div>
            </div>
            <div>
                <div className={`${styles.heading} ${styles.reviewsHeading}`}>Reviews</div>
                <div>{reviews.map((review, i) => <Review key={i} review={review} />)}</div>
            </div>

        </div>
    );
}
