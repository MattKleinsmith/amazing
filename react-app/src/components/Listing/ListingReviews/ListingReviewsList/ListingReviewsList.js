import styles from "./ListingReviewsList.module.css"

import Review from "./Review/Review"

export default function ListingReviewsList({ product, reviews }) {
    if (reviews.length === 0 || reviews[0].product_id !== product.id) return;
    let images = reviews.filter(review => review.review_images.length > 0).map(review => review.review_images[0]);
    images = images.slice(images.length - 4);
    return (
        <div className={styles.wrapper}>
            {images.length > 0 && <div>
                <div className={styles.heading}>Review images</div>
                <div>{images.map((image, i) => <img className={styles.image} key={i} alt={i} src={image.url} />)}</div>
            </div>}
            <div>
                <div className={`${styles.heading} ${styles.reviewsHeading}`}>Top reviews from the United States</div>
                <div className={styles.reviews}>{reviews.map((review, i) => <Review key={i} review={review} />)}</div>
            </div>

        </div>
    );
}
