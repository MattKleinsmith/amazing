import styles from './Register.module.css';

import { useState, useRef, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink, useNavigate, useSearchParams } from 'react-router-dom';

import * as sessionActions from "../../store/session";

export default function RegisterForm() {
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const searchParams = useSearchParams()[0];
    const productId = searchParams.get('productId');
    const quantity = searchParams.get('quantity');

    let source = searchParams.get("source");
    const sourceParts = window.location.search.split("?source=");
    source = sourceParts[sourceParts.length - 1];

    const [isLoaded, setIsLoaded] = useState(false);
    const user = useSelector(state => state.session.user);

    const nameField = useRef();
    const [name, setName] = useState("");
    const [nameError, setNameError] = useState("");

    const emailField = useRef();
    const [email, setEmail] = useState("");
    const [emailError, setEmailError] = useState("");

    const passwordField = useRef();
    const [password, setPassword] = useState("");
    const [passwordError, setPasswordError] = useState("");
    const [showPasswordWarning, setShowPasswordWarning] = useState(true);

    const passwordRepeatField = useRef();
    const [passwordRepeat, setPasswordRepeat] = useState("");
    const [passwordRepeatError, setPasswordRepeatError] = useState("");

    const [bigError, setBigError] = useState("");
    const [submittedEmail, setSubmittedEmail] = useState("");

    const [terms1, setTerms1] = useState("");
    const [terms2, setTerms2] = useState("");

    document.title = "Amazing Registration";

    useEffect(() => {
        setIsLoaded(true);
    }, []);

    useEffect(() => {
        if (!isLoaded) return;
        nameField.current.focus();
    }, [isLoaded]);

    const onClickContinue = async () => {
        let hasErrors = false;

        if (!passwordRepeat) {
            setPasswordRepeatError("Type your password again");
            passwordRepeatField.current.focus();
            hasErrors = true;
        } else if (password !== passwordRepeat) {
            setPasswordRepeatError("Passwords must match");
            passwordRepeatField.current.focus();
            hasErrors = true;
        }

        if (password.length < 6) {
            setPasswordError("Minimum 6 characters required");
            passwordField.current.focus();
            hasErrors = true;
        }

        if (!email) {
            setEmailError("Enter your email");
            emailField.current.focus();
            hasErrors = true;
        } else if (!validateEmail(email)) {
            setEmailError("Invalid email address. Please correct and try again.");
            emailField.current.focus();
            hasErrors = true;
        }

        if (!name) {
            setNameError("Enter your name");
            nameField.current.focus();
            hasErrors = true;
        }

        if (hasErrors) return;

        try {
            await dispatch(sessionActions.register({ fullname: name, email, password }));
            if (productId) {
                navigate(`/addresses/add?productId=${productId}&quantity=${quantity}`);
            }
            else {
                navigate(source ? source : "/");
            }
        }
        catch (responseBody) {
            const backendErrors = Object.entries(responseBody.errors)
                .map(([errorField, errorMessage]) => `${errorField}: ${errorMessage}`);
            if (backendErrors.includes("email: Email has already been used.")) {
                setBigError("You indicated you're a new customer, but an account already exists with the email address");
                setSubmittedEmail(email);
            }
        }
    }

    const validateEmail = (email) => {
        const emailPattern = /\S+@\S+\.\S+/;
        return emailPattern.test(email);
    }

    const onSubmit = (e) => {
        e.preventDefault();
        onClickContinue();
    }

    if (!isLoaded) {
        return <div className={styles.wrapper} >
            <NavLink className={styles.logo} to="/" style={{ textDecoration: 'none' }}>
                <img src="/images/logo_black.png" alt="logo_black" />
            </NavLink>
        </div>
    }

    if (user) {
        return <div className={styles.wrapper} >
            <NavLink className={styles.logo} to="/" style={{ textDecoration: 'none' }}>
                <img src="/images/logo_black.png" alt="logo_black" />
            </NavLink>
            <div>
                You are already logged in.
            </div>
        </div>
    }

    return (
        <>
            <div className={styles.wrapper}>

                <NavLink className={styles.logo} to="/" style={{ textDecoration: 'none' }}>
                    <img src="/images/logo_black.png" alt="logo_black" />
                </NavLink>

                {bigError && <div className={styles.problemWrapper}>
                    <div className={styles.problemIcon} />
                    <div className={styles.problemRight}>
                        <div className={styles.problemTitle}>Email address already in use</div>
                        <div className={styles.problemText}>{bigError}</div>
                        <div className={styles.problemEmail}>{submittedEmail}.</div>
                    </div>
                </div>}

                <form className={styles.form} onSubmit={onSubmit}>
                    <div className={styles.title}>Create account</div>

                    <div className={styles.fieldWrapper}>
                        <label htmlFor="signUpName" className={styles.fieldLabel}>
                            Your name
                        </label>
                        <input
                            ref={nameField}
                            id="signUpName"
                            className={`${styles.fieldInput} ${nameError && styles.errorInput}`}
                            type="text"
                            autoComplete="off"
                            value={name}
                            onChange={(e) => {
                                setNameError("");
                                setName(e.target.value);
                            }}
                            placeholder="First and last name"
                        />
                        {nameError && <div className={styles.errorWrapper}>
                            <div className={styles.errorIcon} />
                            <div className={styles.errorText}>{nameError}</div>
                        </div>}
                    </div>

                    <div className={styles.fieldWrapper}>
                        <label htmlFor="signUpEmail" className={styles.fieldLabel}>
                            Email
                        </label>
                        <input
                            ref={emailField}
                            id="signUpEmail"
                            className={`${styles.fieldInput} ${emailError && styles.errorInput}`}
                            type="text"
                            autoComplete="off"
                            value={email}
                            onChange={(e) => {
                                setEmailError("");
                                setEmail(e.target.value);
                            }}
                        />
                        {emailError && <div className={styles.errorWrapper}>
                            <div className={styles.errorIcon} />
                            <div className={styles.errorText}>{emailError}</div>
                        </div>}
                    </div>

                    <div className={styles.fieldWrapper}>
                        <label htmlFor="signUpPassword" className={styles.fieldLabel}>
                            Password
                        </label>
                        <input
                            ref={passwordField}
                            id="signUpPassword"
                            className={`${styles.fieldInput} ${passwordError && styles.errorInput}`}
                            type="password"
                            value={password}
                            onChange={(e) => {
                                if (e.target.value.length >= 6 && passwordError) {
                                    setShowPasswordWarning(false);
                                    setPasswordError("");
                                }
                                setPassword(e.target.value);
                            }}
                            placeholder="At least 6 characters"
                        />
                        {passwordError && <div className={styles.errorWrapper}>
                            <div className={styles.errorIcon} />
                            <div className={styles.errorText}>{passwordError}</div>
                        </div>}
                        {!passwordError && showPasswordWarning && <div className={styles.errorWrapper}>
                            <div className={styles.warningIcon} />
                            <div className={styles.warningText}>Passwords must be at least 6 characters.</div>
                        </div>}
                    </div>

                    <div className={styles.fieldWrapper}>
                        <label htmlFor="signUpRepeatPassword" className={styles.fieldLabel}>
                            Re-enter password
                        </label>
                        <input ref={passwordRepeatField} id="signUpRepeatPassword" className={`${styles.fieldInput} ${passwordRepeatError && styles.errorInput}`}
                            type="password"
                            value={passwordRepeat}
                            onChange={(e) => {
                                setPasswordRepeatError("");
                                setPasswordRepeat(e.target.value);
                            }}
                        />
                        {passwordRepeatError && <div className={styles.errorWrapper}>
                            <div className={styles.errorIcon} />
                            <div className={styles.errorText}>{passwordRepeatError}</div>
                        </div>}
                    </div>

                    <button className={`${styles.continue} ${styles.noselect}`} type="submit">{email ? "Verify email" : "Continue"}</button>

                    <div className={styles.terms}>By creating an account, you agree to Amazing's <br /> <NavLink onClick={() => setTerms1(true)}>You Must Hire Me Conditions</NavLink> and <NavLink onClick={() => setTerms2(true)}> Just Kidding Notice</NavLink>.</div>

                    {terms1 && <div className={styles.jokeTerms}>There are no terms, I was just kidding.</div>}
                    {terms2 && <div className={styles.jokeTerms2}>Verily, there are no terms.</div>}

                    <div className={styles.innerFooter}>
                        <div className={styles.footerLine} />
                        <div className={styles.already}>
                            <div>Already have an account?</div>
                            <NavLink to="/signin" className={styles.signInLinkWrapper}>Sign in <span className={styles.rightArrowLink} /></NavLink>
                        </div>
                    </div>
                </form>
            </div>

            <div className={styles.footer}>
                <div className={styles.footerLine} />
                <div className={styles.links}>
                    <a rel="noreferrer" target="_blank" href="https://www.linkedin.com/in/matthewkleinsmith/">LinkedIn</a>
                    <a rel="noreferrer" target="_blank" href="https://github.com/MattKleinsmith/">GitHub</a>
                    <a rel="noreferrer" target="_blank" href="https://github.com/MattKleinsmith/amazing/">Project repo</a>
                </div>
                <div className={styles.copyright}>
                    Capstone project by <a href="https://github.com/MattKleinsmith/">Matt Kleinsmith</a> of App Academy
                </div>
            </div>
        </>
    );
}
