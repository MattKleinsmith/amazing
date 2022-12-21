import styles from './Register.module.css';
import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import * as sessionActions from "../../store/session";
import { NavLink, useNavigate } from 'react-router-dom';
import { useRef } from 'react';
import { useEffect } from 'react';

export default function RegisterForm() {
    const dispatch = useDispatch();

    const [isLoaded, setIsLoaded] = useState(false);
    const user = useSelector(state => state.session.user);

    const nameField = useRef();
    const [name, setName] = useState("");
    const [nameError, setNameError] = useState("");
    const [showNameField, setShowNameField] = useState(true);

    const emailField = useRef();
    const [email, setEmail] = useState("");
    const [emailError, setEmailError] = useState("");
    const [showEmailField, setShowEmailField] = useState(true);

    const passwordField = useRef();
    const [password, setPassword] = useState("");
    const [passwordError, setPasswordError] = useState("");
    const [showPasswordField, setShowPasswordField] = useState(false);

    const passwordRepeatField = useRef();
    const [passwordRepeat, setPasswordRepeat] = useState("");
    const [passwordRepeatError, setPasswordRepeatError] = useState("");
    const [showPasswordRepeatField, setShowPasswordRepeatField] = useState(false);

    const [bigError, setBigError] = useState("");

    const [terms1, setTerms1] = useState("");
    const [terms2, setTerms2] = useState("");

    const navigate = useNavigate();

    useEffect(() => {
        setIsLoaded(true);
    }, []);

    useEffect(() => {
        if (!isLoaded) return;
        if (showEmailField)
            emailField.current.focus();
        else
            passwordField.current.focus();
    }, [showEmailField, showPasswordField]);

    const onClickContinue = () => {
        if (!email) {
            setEmailError("Enter your email");
            emailField.current.focus();
            return;
        }

        if (!validateEmail(email)) {
            setBigError("We cannot find an account with that email address");
            return;
        }

        setEmailError("");
        setBigError("");
        setShowPasswordField(true);
        setShowEmailField(false);
    }

    const onClickSignIn = async () => {
        if (!password) {
            setPasswordError("Enter your password");
            passwordField.current.focus();
            return;
        }

        try {
            await dispatch(sessionActions.signIn({ email, password }));
            navigate("/");
        }
        catch (responseBody) {
            const backendErrors = Object.entries(responseBody.errors)
                .map(([errorField, errorMessage]) => `${errorField}: ${errorMessage}`);
            if (backendErrors.includes("Credentials: Email and password did not match")) {
                setBigError("Your password is incorrect");
            }
        }
    }

    const onClickChange = () => {
        setPasswordError("");
        setShowPasswordField(false);
        setShowEmailField(true);
    }

    const validateEmail = (email) => {
        const emailPattern = /\S+@\S+\.\S+/;
        return emailPattern.test(email);
    }

    const onSubmit = (e) => {
        e.preventDefault();
        showEmailField ? onClickContinue() : onClickSignIn();
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
            <div className={styles.wrapper} >

                <NavLink className={styles.logo} to="/" style={{ textDecoration: 'none' }}>
                    <img src="/images/logo_black.png" alt="logo_black" />
                </NavLink>

                {bigError && <div className={styles.problemWrapper}>
                    <div className={styles.problemIcon} />
                    <div className={styles.problemRight}>
                        <div className={styles.problemTitle}>There was a problem</div>
                        <div className={styles.problemText}>{bigError}</div>
                    </div>
                </div>}

                <form className={styles.form} onSubmit={onSubmit}>
                    <div className={styles.title}>Create account</div>

                    {showEmailField && <div className={styles.fieldWrapper}>
                        <label htmlFor="signUpEmail" className={styles.fieldLabel}>
                            Your name
                        </label>
                        <input
                            ref={emailField}
                            id="signUpEmail"
                            className={`${styles.fieldInput} ${emailError && styles.errorInput}`}
                            type="text"
                            value={email}
                            onChange={(e) => {
                                setName(e.target.value);
                                setNameError("");
                            }}
                            placeholder="First and last name"
                        />
                        {emailError && <div className={styles.errorWrapper}>
                            <div className={styles.errorIcon} />
                            <div className={styles.errorText}>{emailError}</div>
                        </div>}
                    </div>}

                    {showEmailField && <div className={styles.fieldWrapper}>
                        <label htmlFor="signUpEmail" className={styles.fieldLabel}>
                            Email
                        </label>
                        <input ref={emailField} id="signUpEmail" className={`${styles.fieldInput} ${emailError && styles.errorInput}`}
                            type="text"
                            value={email}
                            onChange={(e) => {
                                setEmail(e.target.value);
                                setEmailError("");
                            }}
                        />
                        {emailError && <div className={styles.errorWrapper}>
                            <div className={styles.errorIcon} />
                            <div className={styles.errorText}>{emailError}</div>
                        </div>}
                    </div>}

                    {showPasswordField && <div className={styles.email}>
                        <div>{email}</div>
                        <div className={styles.changeEmail} onClick={onClickChange}>Change</div>
                    </div>
                    }

                    {showEmailField && <div className={styles.fieldWrapper}>
                        <label htmlFor="signUpPassword" className={styles.fieldLabel}>
                            Password
                        </label>
                        <input
                            ref={passwordField}
                            id="signUpPassword"
                            className={`${styles.fieldInput} ${passwordError && styles.errorInput}`}
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            placeholder="At least 6 characters"
                        />
                        {passwordError && <div className={styles.errorWrapper}>
                            <div className={styles.errorIcon} />
                            <div className={styles.errorText}>{passwordError}</div>
                        </div>}
                        <div className={styles.errorWrapper}>
                            <div className={styles.warningIcon} />
                            <div className={styles.warningText}>Passwords must be at least 6 characters.</div>
                        </div>
                    </div>}

                    {showEmailField && <div className={styles.fieldWrapper}>
                        <label htmlFor="signUpPassword" className={styles.fieldLabel}>
                            Re-enter password
                        </label>
                        <input ref={passwordField} id="signUpPassword" className={`${styles.fieldInput} ${passwordError && styles.errorInput}`}
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                        {passwordError && <div className={styles.errorWrapper}>
                            <div className={styles.errorIcon} />
                            <div className={styles.errorText}>{passwordError}</div>
                        </div>}
                    </div>}

                    {showEmailField && <div className={`${styles.continue} ${styles.noselect}`} onClick={onClickContinue}>Continue</div>}
                    {showPasswordField && <div className={`${styles.continue} ${styles.noselect}`} onClick={onClickSignIn}>Sign in</div>}

                    {showEmailField && <div className={styles.terms}>By creating an account, you agree to Amazing's <br /> <NavLink onClick={() => setTerms1(true)}>You Must Hire Me Conditions</NavLink> and <NavLink onClick={() => setTerms2(true)}> Just Kidding Notice</NavLink>.</div>}

                    {terms1 && <div className={styles.jokeTerms}>There are no terms, I was just kidding.</div>}
                    {terms2 && <div className={styles.jokeTerms}>Verily, there are no terms.</div>}

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
                    <a href="https://www.linkedin.com/in/matthewkleinsmith/">LinkedIn</a>
                    <a href="https://github.com/MattKleinsmith/">GitHub</a>
                    <a href="https://github.com/MattKleinsmith/amazing/">Project repo</a>
                </div>
                <div className={styles.copyright}>
                    Capstone project by <a href="https://github.com/MattKleinsmith/">Matt Kleinsmith</a> of App Academy
                </div>
            </div>
        </>
    );
}
