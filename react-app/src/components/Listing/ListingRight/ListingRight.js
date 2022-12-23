import styles from "./ListingRight.module.css";

import { useState } from "react";
import { useSelector } from "react-redux";
import { useNavigate } from "react-router";

export default function ListingRight({ product }) {
    const navigate = useNavigate();
    const user = useSelector(state => state.session.user);
    const [quantity, setQuantity] = useState(1);

    return (
        <div className={styles.wrapper}>
            <div className={styles.sellerInfo}>
                <div>{product.seller.fullname}</div>
            </div>
            <div className={styles.title}>{product.title}</div>
            <div className={styles.productPrice}>${(Math.round(product.price * 100) / 100).toFixed(2)}</div>
            {!user || user.id !== product.seller_id ?
                <div className={styles.purchaseOptions}>
                    <label htmlFor="quantity">Quantity</label>
                    <select
                        name="quantity"
                        value={quantity}
                        onChange={(e) => {
                            setQuantity(e.target.value);
                        }}>
                        {[...Array(11).keys()].slice(1).map((num) => (
                            <option
                                key={num}
                                value={num}
                            >
                                {num}</option>))}
                    </select>

                    <div>
                        <button className={styles.buyItNow}
                            onClick={() => { }}
                        >Buy it now</button>
                    </div>
                    <div>
                        <button className={styles.addToCart}
                            onClick={() => {
                            }}>Add to cart</button>
                    </div>
                </div>
                :
                <button onClick={() => navigate(`/your/shop/listing/${product.id}`)}>Edit listing</button>
            }
        </div>
    );
}
