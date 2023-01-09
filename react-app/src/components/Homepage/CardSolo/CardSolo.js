import styles from "./CardSolo.module.css";

import { useDispatch } from "react-redux";
import { useEffect } from "react";
import { getProductsForHomepage } from "../../../store/products";

export default function CardSolo({ product, heading }) {
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getProductsForHomepage())
    }, []);

    return (
        <div className={styles.wrapper}>
            <div className={styles.content}>
                <div className={styles.heading}>{heading}</div>
                <div className={styles.grid}>
                    <div className={styles.tile}>
                        <img className={styles.image} alt="" src={product?.preview_image} />
                        <div className={styles.title}>{product?.title}</div>
                    </div>
                </div>
            </div>
        </div>
    );
}
