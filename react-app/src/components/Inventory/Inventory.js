import styles from "./Inventory.module.css";

import { useEffect } from "react";
import { useDispatch, useSelector } from 'react-redux';

import { getProductsCurrent } from "../../store/productsCurrent";

import InventoryItem from "./InventoryItem/InventoryItem";
import { NavLink } from "react-router-dom";

export default function Inventory() {
    const products = useSelector(state => state.productsCurrent);
    const dispatch = useDispatch();
    useEffect(() => {
        dispatch(getProductsCurrent());
    }, [dispatch]);
    return (
        <div className={styles.wrapper}>
            <div className={styles.bar}>
                <div className={styles.heading}>Manage Inventory</div>
                <div className={styles.addProductWrapper}>
                    <NavLink to="/inventory/add"><button className={styles.addProduct}>Add product</button></NavLink>
                </div>
            </div>
            <div className={styles.inventory}>
                {products.map((product, i) => <InventoryItem key={i} product={product} />)}
            </div>
        </div>
    );
}
