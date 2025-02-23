
Inductive A : Type :=
    | red
    | green

Definition f (x : A) : A :=
    match x with
    | red => green
    | green => red
    end.

Theorem one : forall x : A, x != f(x):
Proof.
    intros. destruct x.
    + simpl.
Qed.