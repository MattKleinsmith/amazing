import styles from "./ListingImages.module.css";

import { useState } from "react";

export default function ListingImages({ product }) {
    const [url, setUrl] = useState(product.image_urls[0]);

    const onClick = (i) => {
        setUrl(product.image_urls[i]);
    };

    return (
        <div className={styles.wrapper}>

            <div className={styles.moreImagesWrapper}>
                {product.image_urls.map((url, i) =>
                    <button className={styles.moreImagesBtn} onClick={() => onClick(i)} key={i} >
                        <img src={url} alt="product_image" className={styles.moreImages} />
                    </button>)}
            </div>

            <div className={styles.defaultImageWrapper}>
                <img src={url} alt="ListingImages" className={styles.defaultImage} />
            </div>

        </div>
    );
}
