import styles from "./Inventory.module.css";

import { useEffect } from "react";

import { useDispatch, useSelector } from 'react-redux';

import { getProductsCurrent } from "../../../store/productsCurrent";

export default function Inventory() {
    const products = useSelector(state => state.productsCurrent);
    const dispatch = useDispatch();
    useEffect(() => {
        dispatch(getProductsCurrent());
    }, [dispatch]);
    return (
        <>
            <div className={styles.wrapper}>
                {products.map((product, i) => <div key={i}>{product.title}</div>)}
            </div>
        </>
    );
}
