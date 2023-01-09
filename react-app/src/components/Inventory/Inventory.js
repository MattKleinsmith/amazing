import styles from "./Inventory.module.css";

import { useEffect } from "react";
import { useDispatch, useSelector } from 'react-redux';

import { getProductsCurrent } from "../../store/productsCurrent";

import InventoryItem from "./InventoryItem/InventoryItem";
import { NavLink } from "react-router-dom";

export default function Inventory() {
    const dispatch = useDispatch();

    const products = useSelector(state => state.productsCurrent);

    useEffect(() => {
        dispatch(getProductsCurrent());
    }, [dispatch]);

    document.title = "Your Product Listings"

    return (
        <div className={styles.wrapper}>
            <div className={styles.bar}>
                {products.length !== 0 && <div className={styles.heading}>Manage product listings</div>}
                {products.length !== 0 && <div className={styles.addProductWrapper}>
                    <NavLink to="/inventory/add"><button className={styles.addProduct}>Add product</button></NavLink>
                </div>}
            </div>
            {products.length !== 0 && <div className={styles.inventory}>
                <div className={styles.columnHeaders}>
                    <div className={styles.image}>Image</div>
                    <div className={styles.title}>Title</div>
                    <div className={styles.date}>
                        <div>Created</div>
                        <div>Updated</div>
                    </div>
                    <div className={styles.price}>Price</div>
                </div>
                <div className={styles.line} />
                {products.map((product, i) => <InventoryItem key={i} product={product} />)}
            </div>}
            {products.length === 0 &&
                <div className={styles.emptyWrapper}>
                    <div className={styles.heading}>You have no product listings.</div>
                    <div className={styles.addProductWrapperEmpty}>
                        <NavLink to="/inventory/add"><button className={styles.addProduct}>Add product</button></NavLink>
                    </div>
                </div>
            }
        </div>
    );
}
