import styles from "./OrderConfirmation.module.css";

import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import { useEffect } from "react";

import { getProductDetails } from "../../store/productDetails";

export default function OrderConfirmation() {
    const user = useSelector(state => state.session.user);
    const purchase = useSelector(state => state.purchases)[0];

    const dispatch = useDispatch();
    const product = useSelector(state => state.productDetails)[purchase.product_id];

    useEffect(() => {
        dispatch(getProductDetails(purchase.product_id));
    }, [dispatch, purchase]);

    if (!product) return;

    return (
        <div className={styles.wrapper}>
            <div>Hello {user.fullname},</div>
            <div>Thank you for shopping with us. You ordererd <NavLink to={`/listing/${product.id}`}>"{product.title}"</NavLink>. We'll send you a confirmation when your item ships.</div>
            <div>Details</div>
            <div>Order {purchase.order_id}</div>
            <div>
                <div>
                    <div>Not yet shipped</div>
                    <div>View order</div>
                </div>
                <div>
                    <div>
                        <div>Ship to:</div>
                        <div></div>
                    </div>
                </div>
            </div>
        </div>
    );
}
