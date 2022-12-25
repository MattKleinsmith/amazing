import styles from "./ListingImages.module.css";

import { useState } from "react";

export default function ListingImages({ product }) {
    const [url, setUrl] = useState(product.image_urls[0]);

    const onMouseEnter = (i) => {
        setUrl(product.image_urls[i]);
    };

    return (
        <div className={styles.wrapper}>

            <div className={styles.thumbnailListWrapper}>
                {product.image_urls.map((url, i) =>
                    <img className={styles.thumbnail} src={url} alt="thumbnail" onMouseEnter={() => onMouseEnter(i)} key={i} />)}
            </div>

            <div className={styles.imageWrapper}>
                <img className={styles.image} src={url} alt="main image" />
            </div>

        </div>
    );
}
