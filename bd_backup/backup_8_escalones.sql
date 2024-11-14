PGDMP     -    6            
    |            8_escalones    10.23    15.2 (               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16579    8_escalones    DATABASE     �   CREATE DATABASE "8_escalones" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Spain.1252';
    DROP DATABASE "8_escalones";
                postgres    false                        0    0    DATABASE "8_escalones"    COMMENT     H   COMMENT ON DATABASE "8_escalones" IS 'Base de datos Trabajo Final POO';
                   postgres    false    2847                        2615    2200    public    SCHEMA     2   -- *not* creating schema, since initdb creates it
 2   -- *not* dropping schema, since initdb creates it
                postgres    false            !           0    0    SCHEMA public    ACL     Q   REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;
                   postgres    false    6            �            1259    16712    escalon_partida    TABLE     �   CREATE TABLE public.escalon_partida (
    nro_escalon integer NOT NULL,
    estado boolean NOT NULL,
    id_tema integer NOT NULL
);
 #   DROP TABLE public.escalon_partida;
       public            postgres    false    6            �            1259    16692    jugador    TABLE     �   CREATE TABLE public.jugador (
    id_jugador integer NOT NULL,
    nombre_jugador character varying NOT NULL,
    avatar character varying NOT NULL
);
    DROP TABLE public.jugador;
       public            postgres    false    6            �            1259    16690    jugador_id_jugador_seq    SEQUENCE     �   CREATE SEQUENCE public.jugador_id_jugador_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.jugador_id_jugador_seq;
       public          postgres    false    6    201            "           0    0    jugador_id_jugador_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.jugador_id_jugador_seq OWNED BY public.jugador.id_jugador;
          public          postgres    false    200            �            1259    16703    jugador_partida    TABLE     �   CREATE TABLE public.jugador_partida (
    id_partida integer NOT NULL,
    id_jugador integer NOT NULL,
    ronda1 integer NOT NULL,
    ronda2 integer NOT NULL
);
 #   DROP TABLE public.jugador_partida;
       public            postgres    false    6            �            1259    16701    jugador_partida_id_partida_seq    SEQUENCE     �   CREATE SEQUENCE public.jugador_partida_id_partida_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public.jugador_partida_id_partida_seq;
       public          postgres    false    6    203            #           0    0    jugador_partida_id_partida_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public.jugador_partida_id_partida_seq OWNED BY public.jugador_partida.id_partida;
          public          postgres    false    202            �            1259    16709    pregunta_partida    TABLE     h   CREATE TABLE public.pregunta_partida (
    id_pregunta integer NOT NULL,
    estado boolean NOT NULL
);
 $   DROP TABLE public.pregunta_partida;
       public            postgres    false    6            �            1259    16615 	   preguntas    TABLE     �  CREATE TABLE public.preguntas (
    id_pregunta integer NOT NULL,
    enunciado_pregunta character varying(255) NOT NULL,
    rta_a character varying(50) NOT NULL,
    rta_b character varying(50) NOT NULL,
    rta_c character varying(50) NOT NULL,
    rta_d character varying(50) NOT NULL,
    rta_correcta character varying(50) NOT NULL,
    tipo_pregunta character varying(100),
    estado_pregunta boolean,
    id_tema integer NOT NULL
);
    DROP TABLE public.preguntas;
       public            postgres    false    6            �            1259    16613    preguntas_id_pregunta_seq    SEQUENCE     �   CREATE SEQUENCE public.preguntas_id_pregunta_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.preguntas_id_pregunta_seq;
       public          postgres    false    6    197            $           0    0    preguntas_id_pregunta_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.preguntas_id_pregunta_seq OWNED BY public.preguntas.id_pregunta;
          public          postgres    false    196            �            1259    16626    temas    TABLE     m   CREATE TABLE public.temas (
    id_tema integer NOT NULL,
    nombre_tema character varying(100) NOT NULL
);
    DROP TABLE public.temas;
       public            postgres    false    6            �            1259    16624    temas_id_tema_seq    SEQUENCE     �   CREATE SEQUENCE public.temas_id_tema_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.temas_id_tema_seq;
       public          postgres    false    199    6            %           0    0    temas_id_tema_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.temas_id_tema_seq OWNED BY public.temas.id_tema;
          public          postgres    false    198            �
           2604    16695    jugador id_jugador    DEFAULT     x   ALTER TABLE ONLY public.jugador ALTER COLUMN id_jugador SET DEFAULT nextval('public.jugador_id_jugador_seq'::regclass);
 A   ALTER TABLE public.jugador ALTER COLUMN id_jugador DROP DEFAULT;
       public          postgres    false    200    201    201            �
           2604    16706    jugador_partida id_partida    DEFAULT     �   ALTER TABLE ONLY public.jugador_partida ALTER COLUMN id_partida SET DEFAULT nextval('public.jugador_partida_id_partida_seq'::regclass);
 I   ALTER TABLE public.jugador_partida ALTER COLUMN id_partida DROP DEFAULT;
       public          postgres    false    202    203    203            �
           2604    16618    preguntas id_pregunta    DEFAULT     ~   ALTER TABLE ONLY public.preguntas ALTER COLUMN id_pregunta SET DEFAULT nextval('public.preguntas_id_pregunta_seq'::regclass);
 D   ALTER TABLE public.preguntas ALTER COLUMN id_pregunta DROP DEFAULT;
       public          postgres    false    197    196    197            �
           2604    16629    temas id_tema    DEFAULT     n   ALTER TABLE ONLY public.temas ALTER COLUMN id_tema SET DEFAULT nextval('public.temas_id_tema_seq'::regclass);
 <   ALTER TABLE public.temas ALTER COLUMN id_tema DROP DEFAULT;
       public          postgres    false    198    199    199                      0    16712    escalon_partida 
   TABLE DATA           G   COPY public.escalon_partida (nro_escalon, estado, id_tema) FROM stdin;
    public          postgres    false    205   #,                 0    16692    jugador 
   TABLE DATA           E   COPY public.jugador (id_jugador, nombre_jugador, avatar) FROM stdin;
    public          postgres    false    201   @,                 0    16703    jugador_partida 
   TABLE DATA           Q   COPY public.jugador_partida (id_partida, id_jugador, ronda1, ronda2) FROM stdin;
    public          postgres    false    203   ],                 0    16709    pregunta_partida 
   TABLE DATA           ?   COPY public.pregunta_partida (id_pregunta, estado) FROM stdin;
    public          postgres    false    204   z,                 0    16615 	   preguntas 
   TABLE DATA           �   COPY public.preguntas (id_pregunta, enunciado_pregunta, rta_a, rta_b, rta_c, rta_d, rta_correcta, tipo_pregunta, estado_pregunta, id_tema) FROM stdin;
    public          postgres    false    197   �,                 0    16626    temas 
   TABLE DATA           5   COPY public.temas (id_tema, nombre_tema) FROM stdin;
    public          postgres    false    199   M1       &           0    0    jugador_id_jugador_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.jugador_id_jugador_seq', 1, false);
          public          postgres    false    200            '           0    0    jugador_partida_id_partida_seq    SEQUENCE SET     M   SELECT pg_catalog.setval('public.jugador_partida_id_partida_seq', 1, false);
          public          postgres    false    202            (           0    0    preguntas_id_pregunta_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.preguntas_id_pregunta_seq', 1, false);
          public          postgres    false    196            )           0    0    temas_id_tema_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.temas_id_tema_seq', 33, true);
          public          postgres    false    198            �
           2606    16708 $   jugador_partida jugador_partida_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.jugador_partida
    ADD CONSTRAINT jugador_partida_pkey PRIMARY KEY (id_partida);
 N   ALTER TABLE ONLY public.jugador_partida DROP CONSTRAINT jugador_partida_pkey;
       public            postgres    false    203            �
           2606    16700    jugador jugador_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.jugador
    ADD CONSTRAINT jugador_pkey PRIMARY KEY (id_jugador);
 >   ALTER TABLE ONLY public.jugador DROP CONSTRAINT jugador_pkey;
       public            postgres    false    201            �
           2606    16623    preguntas preguntas_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.preguntas
    ADD CONSTRAINT preguntas_pkey PRIMARY KEY (id_pregunta);
 B   ALTER TABLE ONLY public.preguntas DROP CONSTRAINT preguntas_pkey;
       public            postgres    false    197            �
           2606    16631    temas temas_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.temas
    ADD CONSTRAINT temas_pkey PRIMARY KEY (id_tema);
 :   ALTER TABLE ONLY public.temas DROP CONSTRAINT temas_pkey;
       public            postgres    false    199            �
           2606    16685    preguntas id_tema    FK CONSTRAINT        ALTER TABLE ONLY public.preguntas
    ADD CONSTRAINT id_tema FOREIGN KEY (id_tema) REFERENCES public.temas(id_tema) NOT VALID;
 ;   ALTER TABLE ONLY public.preguntas DROP CONSTRAINT id_tema;
       public          postgres    false    197    199    2705                  x������ � �            x������ � �            x������ � �            x������ � �         �  x��V�R9=���lm1`>��a!��K{F�h��4�.��8���U;?��e1�^dI�Q�~���3��?�n�Z9�J*#k�+��.�m�,�4.���P��?���PN<ͨ�����Xq��/��Ha�m�8+����Â� ��\EA���T��g#q!>]�lk���ۯ��oN�t�>1�7U��v��Z�0����P��m����lG��n�����(w�K�	�_%C���	Y�=��O2r�L�dũ�}�X�����l�C�䕾'��@��l����=�8"3q����qlL�`9�@L-n��H��j�L�5��E�s���)�m|cKC���ncht�I�шc#)V`%Q��:�� ��r=�N/>����:�8�*Pn���N��Ab��4�rRqQVLre �X���3��S���n��S1v�m�-�{�w���5WI�$O"'./�-��Pd��mY��vk��k�*�^O��#��-T�0X��'�ޔ����p���Ti�gF��b���g�;B?��[S�d�N�X��QI�M���}�wJ�1hZj�zCw�7ب�i�Brz#ub:4�x�TfU��(��8#F.(q���w?�O�F?���.�vF1������F��w��MC?��|�`ϲU �l}� �5�\�*�h��
RY����C�_�E���&=�n���uv6�>�+��*���6\+(9վz]p�Hy��0)P�SWqm��b�cA A���Ld�< К�Mk{�����1�V:�1-+ia�A�3y��d�L��i��ԩ�*��8,��b��������
X'��$�'���9��T#d��A�,�3�C��T+��T��P��Jub�W�/]X_�l����?�|5���q-Ԑ��V]��X�5�M���e�Z5�������[gT���!PX+�x)�a��d�������븓��U�H�a�x��Z�'���Jp����G�WL:o��[S���pB�}G����,�V���*ᱯn�m���>�N����Ë�D*�P���nfZ�F��8��brJV~��7�����#�M3+t����5�؍��s,��iԯR�ԟ��<�1�Бsq�oah�'�vnء Weu��;����`������]b^�ۇ
�ý.�K]7h�s��Oei������Z���AӃg�?�������gK         2  x�M�MN�0��3��	Pm�wYJ[*���%�����n��b�6�(bg�<��	��}�%�׭~z�
vLΰ�YǮՖΡԑ��3��pǑ�q�K(���JO�n���H��g2�[_g���6O��]g���H.a,
	{�oF��{o�>{��Á�~'p�o	��7�l��S�5lCl'�J�ذK�����ڼ�"��Ѥ�G�\���P�	6��u	y�x�fJ"�p��<�
N�&U%�Pr���W��ftQ���.Ui�&�L}5�8w��Q�ߛ���Q'����+_(�/W��(��     