import styles from "./Inventory.module.css";

import { useEffect } from "react";
import { useDispatch, useSelector } from 'react-redux';

import { getProductsCurrent } from "../../store/productsCurrent";

import InventoryItem from "./InventoryItem/InventoryItem";

export default function Inventory() {
    const products = useSelector(state => state.productsCurrent);
    const dispatch = useDispatch();
    useEffect(() => {
        dispatch(getProductsCurrent());
    }, [dispatch]);
    return (
        <>
            <div className={styles.wrapper}>
                {products.map((product, i) => <InventoryItem key={i} product={product} />)}
            </div>
        </>
    );
}
