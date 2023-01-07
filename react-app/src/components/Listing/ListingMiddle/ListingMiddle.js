import styles from "./ListingMiddle.module.css";

import Stars from "../../Stars/Stars";
import Price from "../../Price/Price";

export default function ListingMiddle({ product, reviewPosition }) {
    const onReviewClick = () => {
        window.scrollTo({ top: reviewPosition });
    }

    return (
        <div className={styles.wrapper}>
            <div className={styles.content}>
                <div className={styles.title}>{product.title}</div>
                <div className={styles.seller}>A product from {product.seller.fullname}</div>
                <div className={styles.rating}>
                    <Stars rating={product.avg_rating} />
                    <div onClick={onReviewClick} className={styles.numRatings}>{product.num_ratings} rating{product.num_ratings !== 1 && "s"}</div>
                </div>
                <div className={styles.hr} />
                <div className={styles.price}>
                    <Price product={product} />
                    <div className={styles.count}>(${parseFloat(product.price).toFixed(2)} / Count)</div>
                </div>
                <div className={`prime ${styles.prime}`} />
                <div className={styles.freeReturns}>FREE Returns</div>
                <div className={styles.rewards}><span className={styles.getBack}>Get 5% back ($4.99 in rewards)</span> on the amount charged to your Amazing Prime Rewards Visa Signature Card.</div>
                <div className={styles.hr} />
                <div className={styles.aboutTitle}>About this item</div>
                <ul className={styles.about}>{product.description.split("\n").map((item, i) => { return <li key={i}>{item}</li> })}</ul>
            </div>
        </div>
    );
}
