import styles from "./ListingLeft.module.css";
import ListingImages from "./ListingImages/ListingImages";
import ListingReviews from "./ListingReviews/ListingReviews";

export default function ListingLeft({ product }) {
    return (
        <div className={styles.wrapper}>
            <ListingImages product={product} />
            <ListingReviews product={product} />
        </div>
    );
}
