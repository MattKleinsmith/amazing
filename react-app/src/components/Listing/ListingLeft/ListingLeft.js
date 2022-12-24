import styles from "./ListingLeft.module.css";

import ListingImages from "./ListingImages/ListingImages";

export default function ListingLeft({ product }) {
    return (
        <div className={styles.wrapper}>
            <ListingImages product={product} />
        </div>
    );
}
