import styles from "./Card.module.css";

import { useDispatch } from "react-redux";
import { useEffect } from "react";
import { getProductsForHomepage } from "../../../store/products";

export default function Card({ products, heading }) {
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getProductsForHomepage())
    }, []);

    return (
        <div className={styles.wrapper}>
            <div className={styles.content}>
                <div className={styles.heading}>{heading}</div>
                <div className={styles.grid}>
                    {Object.values(products).slice(0, 2).map((product, i) => <div className={styles.tile} key={i}>
                        <img className={styles.image} alt="" src={product.preview_image} />
                        <div className={styles.title}>{product.title}</div>
                    </div>)}
                </div>
                <div className={styles.grid}>
                    {Object.values(products).slice(2, 4).map((product, i) => <div className={styles.tile} key={i}>
                        <img className={styles.image} alt="" src={product.preview_image} />
                        <div className={styles.title}>{product.title}</div>
                    </div>)}
                </div>
            </div>
        </div>
    );
}
