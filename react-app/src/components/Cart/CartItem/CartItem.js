import styles from "./CartItem.module.css";

import { NavLink } from "react-router-dom";

import Quantity from "./Quantity/Quantity";
import { useDispatch } from "react-redux";
import { deleteCartItem } from "../../../store/cartItems";
import { useState } from "react";

export default function CartItem({ product, quantity }) {
    const dispatch = useDispatch();
    const [isDeleted, setIsDeleted] = useState(false);

    const onDelete = () => {
        dispatch(deleteCartItem(product.id));
        setIsDeleted(true);
    };

    if (!product) return;
    if (isDeleted) return <>
        <div className={styles.deleted}>
            <NavLink to={`/listing/${product.id}`} className={styles.deletedLink}>
                {product.title}
            </NavLink>was removed from Shopping Cart.</div>
        <div className={styles.line} />
    </>;
    return <>
        <div className={styles.wrapper}>
            <div className={styles.left}>
                <NavLink to={`/listing/${product.id}`}><img className={styles.image} src={product.preview_image} alt="" /></NavLink>
                <div className={styles.middle}>
                    <div>
                        <div className={styles.title}><NavLink className={styles.title} to={`/listing/${product.id}`} >{product.title}</NavLink></div>
                        <div className={styles.inStock}>In Stock</div>
                        <div className={styles.shippedFrom}>Shipped from: {product.seller.fullname}</div>
                        <div className={styles.shippedFrom}>Gift options not available.</div>
                        <div className={styles.row}>
                            <Quantity productId={product.id} quantity={quantity} />
                            <div className={styles.verticalBar} />
                            <div className={styles.delete}
                                onClick={onDelete}
                            >
                                Delete
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div className={styles.price}>${parseFloat(product.price * quantity).toFixed(2)}</div>
        </div>
        <div className={styles.line} />
    </>;
}
