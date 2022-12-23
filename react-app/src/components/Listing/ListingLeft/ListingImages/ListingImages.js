import styles from "./ListingImages.module.css";
import { useState } from "react";

export default function ListingImages({ product }) {
    const [url, setUrl] = useState(product.preview_image);

    const onClickHandler = (productImageId) => {
        const image = product.product_images.find(image => image.id === productImageId);
        setUrl(image.url);
    };

    if (!product.product_images) return;
    return (
        <div className={styles.wrapper}>
            <div type='checkbox' className={styles.moreImagesWrapper}>
                {product.product_images.map((product_image, i) =>
                    <button className={styles.moreImagesBtn} onClick={() => onClickHandler(product_image.id)} key={i} >
                        <img src={product_image.url} alt="ListingImages" className={styles.moreImages} />
                    </button>)}
            </div>
            <div className={styles.defaultImageWrapper}>
                <img src={url} alt="ListingImages" className={styles.defaultImage} />
            </div>
        </div >
    );
}
