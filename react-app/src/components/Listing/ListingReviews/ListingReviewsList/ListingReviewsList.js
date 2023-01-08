import styles from "./ListingReviewsList.module.css"

import Review from "./Review/Review"

export default function ListingReviewsList({ product, reviews }) {
    if (reviews.length === 0 || reviews[0].product_id !== product.id) return;
    const images = reviews.reduce((images, review) => images.concat(review.review_images), []).slice(0, 4);
    return (
        <div className={styles.wrapper}>
            {images.length > 0 && <div>
                <div className={styles.heading}>Review images</div>
                <div className={styles.reviewImages}>{images.map((image, i) => <img src={image.url} className={styles.image} key={i} alt={i} />)}</div>
            </div>}
            <div>
                <div className={`${styles.heading} ${styles.reviewsHeading}`}>Top reviews from the United States</div>
                <div className={styles.reviews}>{reviews.map((review, i) => <Review key={i} review={review} />)}</div>
            </div>

        </div>
    );
}
