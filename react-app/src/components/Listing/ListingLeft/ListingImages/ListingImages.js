import styles from "./ListingImages.module.css";

import { useRef, useState } from "react";

export default function ListingImages({ product }) {
    const [url, setUrl] = useState(product.image_urls[0]);
    const firstThumbnailRef = useRef();
    const [thumbnail, setThumbnail] = useState();

    const onMouseEnter = (i, e) => {
        setUrl(product.image_urls[i]);
        firstThumbnailRef.current.classList.remove(styles.thumbnailHover);
        if (thumbnail) thumbnail.classList.remove(styles.thumbnailHover);
        e.target.classList.add(styles.thumbnailHover);
        setThumbnail(e.target);
    };

    return (
        <div className={styles.wrapper}>

            <div className={styles.thumbnailListWrapper}>
                {product.image_urls.map((url, i) => {
                    if (i === 0) {
                        return <img ref={firstThumbnailRef} className={`${styles.thumbnail} ${styles.thumbnailHover}`} src={url} alt="thumbnail" onMouseEnter={(e) => onMouseEnter(i, e)} key={i} />
                    } else {
                        return <img className={`${styles.thumbnail}`} src={url} alt="thumbnail" onMouseEnter={(e) => onMouseEnter(i, e)} key={i} />
                    }
                })}
            </div>

            <div className={styles.imageWrapper}>
                <img className={styles.image} src={url} alt="main" />
            </div>

        </div>
    );
}
