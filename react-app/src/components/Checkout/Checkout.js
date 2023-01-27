import styles from "./Checkout.module.css";

import { useDispatch, useSelector } from 'react-redux';
import { useEffect, useState } from "react";
import { NavLink, useNavigate } from "react-router-dom";

import { getProductDetails } from "../../store/productDetails";
import { postOrder } from "../../store/orders";
import { setAddressModal } from "../../store/ui";
import { clearCart } from "../../store/cartItems";

import AddressSelector from "./AddressSelector/AddressSelector";
import OrderSummary from "./OrderSummary/OrderSummary";
import BottomSummary from "./BottomSummary/BottomSummary";
import CheckoutItemList from "./CheckoutItemList/CheckoutItemList";

export default function Checkout() {
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const [addressIdx, setAddressIdx] = useState(0);
    const [showAddressSelector, setShowAddressSelector] = useState(false);

    const cartItems = useSelector(state => state.cartItems);
    const productDetails = useSelector(state => state.productDetails);
    const addresses = useSelector(state => Object.values(state.addresses));

    const productIds = Object.keys(cartItems);

    useEffect(() => {
        productIds.forEach(productId => dispatch(getProductDetails(productId)))
        // eslint-disable-next-line
    }, [dispatch, cartItems]);

    if (productIds.length === 0)
        return <div className={styles.wrapper}>
            <div className={styles.content}>
                <div className={styles.heading}>Your Amazing Cart is empty.</div>
                <NavLink to="/" className={styles.continue}>Continue shopping</NavLink>
            </div>
        </div>;

    const onPlaceOrder = async () => {
        if (addresses.length === 0) {
            onAddAddress();
        }
        else {
            try {
                const address = `${addresses[addressIdx].fullname}\n${addresses[addressIdx].address.toUpperCase()}\n${addresses[addressIdx].city.toUpperCase()}, ${addresses[addressIdx].state.toUpperCase()} ${addresses[addressIdx].zipcode.toUpperCase()}\n${addresses[addressIdx].region}`;
                await dispatch(postOrder({ address, cart: cartItems }));
                dispatch(clearCart());
                navigate("/order-confirmation");
            } catch (e) {
                console.log("Order failed:", e);
            }
        }
    };

    const onAddAddress = () => {
        dispatch(setAddressModal(true));
    }

    const numItems = productIds.reduce((sum, productId) => sum += cartItems[productId], 0);
    const subtotal = productIds.reduce((sum, productId) => sum += productDetails[productId]?.price * cartItems[productId], 0);
    const taxRate = 0.08687954888;
    const taxes = subtotal * taxRate;
    const total = subtotal + taxes;

    let deliveryDate = new Date();
    deliveryDate.setDate(deliveryDate.getDate() + 2);
    let nextDeliveryDate = new Date(deliveryDate);
    nextDeliveryDate.setDate(nextDeliveryDate.getDate() + 1);
    const deliveryDateBig = deliveryDate.toLocaleDateString('en-us', { month: "short", day: "numeric", year: "numeric" });
    deliveryDate = deliveryDate.toLocaleDateString('en-us', { weekday: "long", month: "short", day: "numeric" });
    nextDeliveryDate = nextDeliveryDate.toLocaleDateString('en-us', { weekday: "long", month: "short", day: "numeric" });

    return <>
        <div className={styles.headerWrapper}>
            <div className={styles.header}>
                <NavLink to="/" className={styles.logo}><img src="https://d1irxr40exwge2.cloudfront.net/logo_black.png" alt="logo_black" /></NavLink>
                <div className={styles.checkout}>Checkout <span className={styles.checkoutItem}>(<NavLink to="/cart" className={styles.checkoutLink}>{numItems} item{numItems > 1 && "s"}</NavLink>)</span></div>
                <div className={styles.secureIconWrapper}>
                    <img src="https://d1irxr40exwge2.cloudfront.net/secure.png" alt="Secure icon" height="20px" />
                </div>
            </div>
        </div>

        <div className={styles.wrapperWrapper}>

            <div className={styles.wrapper}>

                <div className={styles.content}>

                    {showAddressSelector ?
                        <>
                            <div>
                                <div className={styles.step}>
                                    <div className={`${styles.stepHeader} ${styles.stepNumber} ${styles.orange}`}>1</div>

                                    <div className={styles.addressSelectorTitleWrapper}>
                                        <div className={`${styles.stepHeader} ${styles.stepTitle} ${styles.orange} ${styles.chooseAddressTitle}`}>Choose a shipping address</div>
                                        <div className={styles.simpleFlex}>
                                            <div className={`${styles.changeLink}`} onClick={() => setShowAddressSelector(false)}>Close</div>
                                            <div className={styles.close} onClick={() => setShowAddressSelector(false)} />
                                        </div>
                                    </div>
                                </div>

                                <div>
                                    <AddressSelector addressIdx={addressIdx} setAddressIdx={setAddressIdx} addresses={addresses} />
                                </div>
                            </div>
                        </>
                        :
                        <>
                            <div className={styles.step}>
                                <div className={`${styles.stepHeader} ${styles.stepNumber}`}>1</div>
                                <div className={`${styles.stepHeader} ${styles.stepTitle}`}>Shipping address</div>

                                {addresses.length > 0 ?
                                    <>
                                        <div className={`${styles.stepBody}`}>
                                            <div>{addresses[addressIdx].fullname}</div>
                                            <div>{addresses[addressIdx].address.toUpperCase()}</div>
                                            <div>{addresses[addressIdx].city.toUpperCase()}, {addresses[addressIdx].state.toUpperCase()} {addresses[addressIdx].zipcode.toUpperCase()}</div>
                                        </div>
                                        <div className={`${styles.changeLink}`} onClick={() => setShowAddressSelector(true)}>Change</div>
                                    </>
                                    :
                                    <div className={`${styles.addAddress}`}>Add an address</div>
                                }
                            </div>
                        </>
                    }

                    <div className={`${styles.line}`} />

                    <div className={styles.step}>
                        <div className={`${styles.stepHeader} ${styles.stepNumber}`}>2</div>
                        <div className={`${styles.stepHeader} ${styles.stepTitle}`}>Payment method</div>
                        <div className={`${styles.stepBody}`}>
                            <div className={`${styles.creditCard}`}>
                                <img src="https://ducksybucket.s3.amazonaws.com/AmazonPrimeRewardsCardArt._CB485937007_.png" alt="credit card" />
                                <div>
                                    <div>Amazing Prime Rewards Visa Signature Card <span className={styles.endingIn}>ending in DEMO</span></div>
                                    <div className={styles.earn}>Earns 5% back</div>
                                </div>
                            </div>
                            <div className={styles.billing}>Billing address: Same as shipping address.</div>
                        </div>
                    </div>

                    <div className={`${styles.line}`} />

                    <div className={styles.step}>
                        <div className={`${styles.stepHeader} ${styles.stepNumber}`}>3</div>
                        <div>

                            <div className={`${styles.stepHeader} ${styles.lastStepTitle}`}>Review items and shipping</div>

                            <CheckoutItemList productDetails={productDetails} cartItems={cartItems} deliveryDateBig={deliveryDateBig} deliveryDate={deliveryDate} productIds={productIds} nextDeliveryDate={nextDeliveryDate} />

                            <BottomSummary addresses={addresses} onPlaceOrder={onPlaceOrder} total={total} />

                        </div>
                    </div>

                </div>

                <OrderSummary addresses={addresses} onPlaceOrder={onPlaceOrder} numItems={numItems} subtotal={subtotal} taxes={taxes} total={total} />

            </div>

        </div>
    </>;
}
