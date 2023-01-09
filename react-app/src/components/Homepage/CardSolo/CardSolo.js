import styles from "./CardSolo.module.css";

import { NavLink } from "react-router-dom";

export default function CardSolo({ product, heading }) {
    return (
        <div className={styles.wrapper}>
            <div className={styles.content}>
                <div className={styles.heading}>{heading}</div>
                <div className={styles.grid}>
                    <NavLink to={`/listing/${product?.id}`} className={styles.tile}>
                        <img className={styles.image} alt="" src={product?.preview_image} />
                        <div className={styles.title}>{product?.title}</div>
                    </NavLink>
                </div>
            </div>
        </div>
    );
}
