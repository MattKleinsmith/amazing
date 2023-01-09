import styles from "./Card.module.css";

import { NavLink } from "react-router-dom";

export default function Card({ products, heading, url }) {
    return (
        <div className={styles.wrapper}>
            <div className={styles.content}>
                <div className={styles.heading}><NavLink to={url} className={styles.headingLink}>{heading}</NavLink></div>
                <div className={styles.grid}>
                    {Object.values(products).slice(0, 2).map((product, i) => <NavLink to={`/listing/${product.id}`} className={styles.tile} key={i}>
                        <img className={styles.image} alt="" src={product.preview_image} />
                        <div className={styles.title}>{product.title}</div>
                    </NavLink>)}
                </div>
                <div className={styles.grid}>
                    {Object.values(products).slice(2, 4).map((product, i) => <NavLink to={`/listing/${product.id}`} className={styles.tile} key={i}>
                        <img className={styles.image} alt="" src={product.preview_image} />
                        <div className={styles.title}>{product.title}</div>
                    </NavLink>)}
                </div>
            </div>
        </div>
    );
}
